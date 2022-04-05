from django.contrib import admin
from .models import Product, Category
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')
    list_filter = ('artist', 'label', 'title')
    search_fields = ['title', 'artist']
    list_display = ('title', 'artist', 'slug', 'label', 'price')


# Register your models here.
# admin.site.register(Product)
admin.site.register(Category)
