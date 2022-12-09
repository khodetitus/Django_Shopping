from django.contrib import admin
from .models import Category, Product, ProductFeature, Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductFeature)
admin.site.register(Comment)
