from django.contrib import admin
from .models import Order, OrderItem, Coupon
from core.admin import BaseAdmin


@admin.register(Order)
class OrderAdmin(BaseAdmin):
    list_display = ('paid', 'discount', 'created')
    search_fields = ('paid', 'discount', 'created')
    list_filter = ('paid', 'discount', 'created')
    ordering = ('paid', 'discount', 'created')
    autocomplete_fields = ('user',)


@admin.register(OrderItem)
class OrderItemAdmin(BaseAdmin):
    list_display = ('product', 'price', 'quantity')
    search_fields = ('product', 'price', 'quantity')
    list_filter = ('product', 'price', 'quantity')
    ordering = ('product', 'price', 'quantity')
    autocomplete_fields = ('product', 'order')


@admin.register(Coupon)
class CouponAdmin(BaseAdmin):
    list_display = ('order', 'discount', 'active', 'code')
    search_fields = ('order', 'discount', 'active', 'code')
    list_filter = ('order', 'discount', 'active', 'code')
    ordering = ('order', 'discount', 'active', 'code')
    autocomplete_fields = ('order',)
