from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=250)
    

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    artist = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField(auto_now=False)
    # rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    audio_file = models.FileField(blank=True, null=True)
    audio_link = models.FileField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
