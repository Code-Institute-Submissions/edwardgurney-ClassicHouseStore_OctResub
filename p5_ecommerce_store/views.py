from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Product, Bag, BagItem, Category
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

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
					userbag = Bag.object.get(user=self.request.user, state='open')
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

def signup_view(request):
	unsubmitted_form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/login')
		else:
			print(form.errors)
			context = {
				'form': form
			}
			return render(request, 'registration/signup.html', context)
	context = {
				'form': unsubmitted_form
			}
	return render(request, 'registration/signup.html', context)
	
	


	
# def basket_view(request):
#     return render(request, 'p5_ecommerce_store/basket.html')
