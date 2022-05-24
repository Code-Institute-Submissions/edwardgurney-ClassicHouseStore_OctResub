from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

from decimal import Decimal


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    artist = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    product_ID = models.CharField(max_length=200, default="", editable=True)
    description = models.TextField()
    release_date = models.DateField(auto_now=False)
    image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    preview_audio_file = models.FileField(blank=True, null=True)
    preview_audio_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    @property
    def average_rating(self):
        try:
            total_rating = 0
            for rating in Rating.objects.filter(product=self):
                total_rating = total_rating + rating.rating_number
            return total_rating / Rating.objects.filter(product=self).count()
        except Exception:
            return "There are no ratings yet, be the first to rate this record"


class Order(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.ForeignKey(
        'ShippingAddress',
        on_delete=models.SET_NULL,
        null=True, blank=True)

    def __str__(self):
        return f"{self.order_number}"


class BagItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    bag = models.ForeignKey('Bag', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

    @property
    def get_bag_item_total(self):
        return Decimal(self.product.price) * Decimal(self.quantity)


class Bag(models.Model):
    STATE = (
        ('open', 'open'),
        ('checkout', 'checked_out'),
        ('closed', 'closed')
    )
    bag_items = models.ManyToManyField('Product', through='BagItem')
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    order = models.OneToOneField('Order', on_delete=models.SET_NULL, null=True,
                                 blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(choices=STATE, max_length=15, default='open')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True,
                             null=True)

    @property
    def is_empty(self):
        if self.bagitem_set.all().count() > 0:
            return False
        return True

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        pending_total = Decimal(0)
        for item in self.bagitem_set.all():
            pending_total = Decimal(pending_total) + Decimal(
                            item.get_bag_item_total)
        self.total = pending_total
        super(Bag, self).save(*args, **kwargs)


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    house_number = models.CharField(max_length=20)
    address_1 = models.CharField(max_length=250)
    address_2 = models.CharField(max_length=250, null=True, blank=True)
    town_or_city = models.CharField(max_length=100)
    county = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating_number = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.product} rated {self.rating_number}'


class NewsLetterSubs(models.Model):
    subscription_date = models.DateTimeField(auto_now_add=True)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.email_address}"
