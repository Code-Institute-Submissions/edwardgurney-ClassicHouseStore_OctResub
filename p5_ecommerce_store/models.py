from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'
        
    name = models.CharField(max_length=250)
    

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    artist = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    product_ID = models.CharField(max_length=200, default="", editable=True)
    description = models.TextField()
    release_date = models.DateField(auto_now=False)
    # rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    audio_file = models.FileField(blank=True, null=True)
    audio_link = models.FileField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey('user', on_delete=models.CASCADE)
    bag = models.OneToOneField('bag', on_delete=models.SET_NULL)
    order_date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.ForeignKey('ShippingAddress', on_delete=model.SET_NULL)


    def __str__(self):
        return self.order_number

class BagItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    bag = models.ForeignKey('Bag', on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Bag(models.Model):
    bag_items = models.ManyToManyField('Product', through='BagItem')
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.id

class ShippingAddress(models.Model):
    user = models.ForeignKey('User', on_delete=models.CACADE)
    house_number = models.CharField(max_length=20)
    address_1 = models.CharField(max_length=250)
    address_2 = models.CharField(max_length=250)
    town_or_city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user

