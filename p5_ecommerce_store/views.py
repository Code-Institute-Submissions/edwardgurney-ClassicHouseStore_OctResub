from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import (Product, Bag, BagItem, Category, ShippingAddress,
					Rating)
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import AddressForm, SignupForm
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
stripe.api_key = settings.STRIPE_SECRET_KEY

class StoreFrontView(generic.ListView):
	template_name = 'p5_ecommerce_store/index.html'
	queryset = Product.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['allcategories'] = Category.objects.all()
		return context

class CategoryView(generic.DetailView):
	template_name = 'p5_ecommerce_store/index.html'
	model = Category

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['allcategories'] = Category.objects.all()
		context['object_list'] = Product.objects.filter(category=self.get_object())
		return context

class ProductDetailView(generic.DetailView):
	model = Product
	template_name = 'p5_ecommerce_store/product_detail.html'

class BasketView(View):
	template_name = 'p5_ecommerce_store/basket.html'
	model = Bag

	def get(self, request, *args, **kwargs):
		current_bag = self.get_object()
		print(current_bag)
		product_id = request.GET.get('product_id')
		print(product_id)
		user_quantity = int(request.GET.get('quantity', 1))
		print(user_quantity)
		if product_id:
			current_product = get_object_or_404(Product, id=product_id)
			print(current_product)
			if user_quantity > 0:
				current_bag_item, created = BagItem.objects.get_or_create(bag=current_bag, product=current_product)
				current_bag_item.quantity = user_quantity
				current_bag_item.save()
				print(current_bag_item)
				current_bag.save()
			else:
				try:
					bag_item = BagItem.objects.get(bag=current_bag,  product=current_product)
					bag_item.delete()
					current_bag.save()
				except BagItem.DoesNotExist:
					pass
		context ={
			'object': current_bag
		}
		return render(request, self.template_name, context)

	def get_object(self, *args, **kwargs):
		old_bag_id = self.request.session.get('bag_id', None)
		if old_bag_id is None:
			if self.request.user.is_authenticated:
				try:
					userbag = Bag.objects.get(user=self.request.user, state='open')
					bag = userbag
				except Bag.DoesNotExist:
					bag = Bag()
					bag.user = self.request.user
					bag.save()		
			else:
				bag = Bag()
				bag.save()
			self.request.session['bag_id'] = bag.id
		else:
			bag = Bag.objects.get(id=old_bag_id)
			if self.request.user.is_authenticated:
				if bag.user is None:
					bag.user = self.request.user
					bag.save()
				elif bag.user != self.request.user:
					bag = Bag()
					bag.user = self.request.user
					bag.save()
					self.request.session['bag_id'] = bag.id		

		return bag

def send_user_email(subject, message, recipient):
	send_mail = EmailMessage(subject, message, to=[recipient], from_email=settings.EMAIL_HOST_USER)
	send_mail.content_subtype = 'html'
	try:
		send_mail.send()
	except Exception as e:
		print(e)
		pass


def signup_view(request):
	unsubmitted_form = SignupForm()
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			message = get_template('p5_ecommerce_store/signup_confirmation.html').render({})
			subject = "Thankyou for signing up"
			recipient = form.instance.email

			send_user_email(subject, message, recipient)
			return HttpResponseRedirect('/login')
		else:
			context = {
				'form': form
			}
			return render(request, 'registration/signup.html', context)
	context = {
				'form': unsubmitted_form
			}
	return render(request, 'registration/signup.html', context)

class CheckoutView(LoginRequiredMixin, SingleObjectMixin, View):
	template_name = 'p5_ecommerce_store/checkout.html'
	model = Bag

	def get(self, request, *args, **kwargs):

		context = {}
		context['object'] = self.get_object()
		context['allcategories'] = Category.objects.all()
		context['form'] = AddressForm(self.request.POST, None)
		context['shipping_addresses'] = ShippingAddress.objects.filter(user=request.user)
		return render(request, self.template_name, context)


	def post(self, request, *args, **kwargs):
		logged_user = request.user
		if 'user_address_selection' in request.POST:
			return HttpResponseRedirect(f"/payment/{self.get_object().id}")
		form = AddressForm(request.POST)
		if form.is_valid():	
			form.instance.user = logged_user
			form.save()
		context = {}
		context['object'] = self.get_object()
		context['allcategories'] = Category.objects.all()
		context['form'] = AddressForm(self.request.POST, None)

		return render(request, self.template_name, context)

@login_required
def payment_view(request, pk):
	context = {}
	context['client_secret'] = create_payment_intent(pk)
	context['bag_id'] = pk
	context['return_url'] = reverse_lazy('checkout_complete', kwargs={'pk':pk})
	print(request.build_absolute_uri(reverse_lazy('checkout_complete', kwargs={'pk':pk})))
	context['public_stripe'] = settings.STRIPE_PUBLIC_KEY
	return render(request, "p5_ecommerce_store/payment.html", context)

def create_payment_intent(pk):
	bag = get_object_or_404(Bag, id=pk)
	try:
		# Create a PaymentIntent with the order amount and currency
		intent = stripe.PaymentIntent.create(
			amount=int(bag.total*100),
			currency='gbp',
			automatic_payment_methods={
				'enabled': True,
			},
		)
		return intent['client_secret']
	except Exception as e:
		print(e)
		return None

def checkout_complete(request, pk):
	context = {}
	return render(request, "p5_ecommerce_store/thankyou.html", context)
	
@login_required
def rate_record(request, pk):
	rated_product = get_object_or_404(Product, id=pk)
	new_rating, created = Rating.objects.get_or_create(user=request.user, product=rated_product)
	user_rating = request.POST.get('rate')
	new_rating.rating_number = user_rating
	new_rating.save()
	return HttpResponseRedirect(f'/product_detail/{pk}')


def search_view(request):
	template_name = 'p5_ecommerce_store/index.html'
	search_item = request.GET.get('search_input')
	title_filter = Product.objects.filter(title__contains=search_item)
	artist_filter = Product.objects.filter(artist__contains=search_item)
	all_queryset = title_filter | artist_filter
	context = {}
	context['allcategories'] = Category.objects.all()
	context['object_list'] = all_queryset
	return render(request, template_name, context)
