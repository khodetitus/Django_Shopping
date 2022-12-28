from django.contrib import admin
from .models import Category, Product, ProductFeature, Comment
from core.admin import BaseAdmin


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    list_display = ('name', 'sub_category', 'is_sub')
    search_fields = ('name', 'sub_category', 'is_sub')
    list_filter = ('name', 'sub_category', 'is_sub')
    ordering = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    list_display = ("name", "price", "stock", "is_deleted", "is_active", "is_available", "created")
    search_fields = ("name", "price", "stock", "is_deleted", "is_active", "is_available", "created")
    list_filter = ("name", "price", "stock", "is_deleted", "is_active", "is_available", "created")
    ordering = ("name",)
    autocomplete_fields = ('category',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProductFeature)
class ProductFeatureAdmin(BaseAdmin):
    list_display = ("product", "color", "type", "material")
    search_fields = ("product", "color", "type", "material")
    list_filter = ("product", "color", "type", "material")
    ordering = ("product", "color", "type", "material")
    autocomplete_fields = ('product',)


@admin.register(Comment)
class CommentAdmin(BaseAdmin):
    list_display = ("user", "product", "title")
    search_fields = ("user", "product", "title")
    list_filter = ("user", "product", "title")
    ordering = ("user", "product", "title")
    autocomplete_fields = ('user', 'product')
