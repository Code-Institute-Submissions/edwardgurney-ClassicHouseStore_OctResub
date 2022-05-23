from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import (Product, Bag, BagItem, Category, ShippingAddress,
                     Rating, Order)
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import AddressForm, SignupForm, NewsLetterForm
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from django.contrib import messages
from django.views.generic.base import TemplateView
stripe.api_key = settings.STRIPE_SECRET_KEY


class StoreFrontView(generic.ListView):
    template_name = 'p5_ecommerce_store/index.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('I got here')
        context['allcategories'] = Category.objects.all()
        context['newsletter_form'] = NewsLetterForm()
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


def mergebags(queryset):
    current_bag = queryset[0]
    for bag in queryset[1:]:
        for item in bag.bagitem_set.all():
            if current_bag.bagitem_set.filter(product=item.product).exists():
                current_bag_item = current_bag.bagitem_set.filter(product=item.product)[0]
                current_bag_item.quantity += item.quantity
            else:
                item.bag = current_bag
        bag.state = 'closed'
    bag.save()
    current_bag.save()


class BasketView(View):
    template_name = 'p5_ecommerce_store/basket.html'
    model = Bag

    def get(self, request, *args, **kwargs):
        current_bag = self.get_object()
        product_id = request.GET.get('product_id')
        user_quantity = int(request.GET.get('quantity', 1))
        if product_id:
            current_product = get_object_or_404(Product, id=product_id)
            if user_quantity > 0:
                current_bag_item, created = BagItem.objects.get_or_create(bag=current_bag,
                                            product=current_product)
                current_bag_item.quantity = user_quantity
                current_bag_item.save()
                current_bag.save()
            else:
                try:
                    bag_item = BagItem.objects.get(bag=current_bag,  product=current_product)
                    bag_item.delete()
                    current_bag.save()
                except BagItem.DoesNotExist:
                    pass
        context = {
            'object': current_bag
        }
        return render(request, self.template_name, context)

    def get_object(self, *args, **kwargs):
        old_bag_id = self.request.session.get('bag_id', None)
        if old_bag_id is None:
            if self.request.user.is_authenticated:
                try:
                    userbag = Bag.objects.filter(user=self.request.user, state='open')
                    if userbag.count() > 1:
                        mergebags(userbag)
                    bag = userbag[0]
                except IndexError:
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
        pass


def signup_view(request):
    unsubmitted_form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            message = get_template('p5_ecommerce_store/signup_confirmation.html').render()
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
        if not self.get_object().is_empty:
            context = {}
            context['object'] = self.get_object()
            context['allcategories'] = Category.objects.all()
            context['form'] = AddressForm()
            context['shipping_addresses'] = ShippingAddress.objects.filter(user=request.user)
            return render(request, self.template_name, context)
        else:
            return HttpResponseRedirect('/')


    def post(self, request, *args, **kwargs):
        logged_user = request.user
        bag = self.get_object()
        if 'user_address_selection' in request.POST:
            address = ShippingAddress.objects.get(id=request.POST.get('address'))
            if address is None:
                return HttpResponseRedirect(f"/checkout/{bag.id}")
            if bag.order == None:
                new_order = Order.objects.create(
                order_number = bag.id,
                customer = bag.user,
                order_total = bag.total,
                shipping_address = address
                )
                bag.order = new_order
                bag.save()
            else:
                order = bag.order
                order.order_total = bag.total
                order.shipping_address = address
                order.save()
                return HttpResponseRedirect(f"/payment/{bag.order.id}")
        form = AddressForm(request.POST)
        if form.is_valid():
            form.instance.user = logged_user
            form.save()
            context = {}
            context['object'] = bag
            context['allcategories'] = Category.objects.all()
            context['form'] = AddressForm()
            return HttpResponseRedirect(f"/checkout/{bag.id}")
        else:
            context = {}
            context['object'] = bag
            context['allcategories'] = Category.objects.all()
            context['form'] = form
            context['shipping_addresses'] = ShippingAddress.objects.filter(user=request.user)
            return render(request, self.template_name, context)


@login_required
def payment_view(request, pk):
    order = get_object_or_404(Order, id=pk)
    if not order.bag.is_empty:
        context = {}
        context['client_secret'] = create_payment_intent(request, pk)
        context['bag_id'] = order.bag.id
        context['order'] = order
        context['return_url'] = "%s%s" % (settings.BASE_URL, reverse_lazy('checkout_complete', kwargs={'pk':pk}))
        context['public_stripe'] = settings.STRIPE_PUBLIC_KEY
        return render(request, "p5_ecommerce_store/payment.html", context)
    else:
        return HttpResponseRedirect('/')


def create_payment_intent(request, pk):
    order = get_object_or_404(Order, id=pk)
    try:
        # Create a PaymentIntent with the order amount and currency
        intent = stripe.PaymentIntent.create(
            amount=int(order.order_total*100),
            currency='gbp',
            automatic_payment_methods={'enabled': True, },
        )

        return intent['client_secret']
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
        return None


def checkout_complete(request, pk):
    order = get_object_or_404(Order, id=pk)
    bag = order.bag
    bag.state = 'checkout'
    bag.save()
    try:
        del request.session['bag_id']
    except Exception:
        pass
    message = get_template('p5_ecommerce_store/order_confirmation_email.html').render({'order':order})
    subject = "Your Order Was Sucessful"
    recipient = request.user.email
    send_user_email(subject, message, recipient)
    context = {
        'order':order
    }
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


class SiteMapView(TemplateView):
    template_name = "p5_ecommerce_store/sitemap.html"


def news_letter_subscription(request):
    form = NewsLetterForm(request.POST)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'You successfully subscribed, thanks')
    else:
        messages.add_message(request, messages.WARNING, 'Sorry, an error occured')
    return HttpResponseRedirect('/')
