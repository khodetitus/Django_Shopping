from django.contrib import admin
from .models import Category, Product, ProductFeature, Comment
from core.admin import BaseAdmin

admin.site.register(ProductFeature)
admin.site.register(Comment)


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    list_display = ("name", "price", "stock", "is_deleted", "is_active", "is_available")
    autocomplete_fields = ("category",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
