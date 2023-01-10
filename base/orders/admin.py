from django.contrib import admin
from .models import Order, OrderItem, Coupon
from core.admin import BaseAdmin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(BaseAdmin):
    list_display = ('paid', 'discount', 'created')
    search_fields = ('paid', 'discount', 'created')
    list_filter = ('paid', 'discount', 'created')
    ordering = ('paid', 'discount', 'created')
    autocomplete_fields = ('user',)
    inlines = (OrderItemInline,)


@admin.register(Coupon)
class CouponAdmin(BaseAdmin):
    list_display = ('order', 'discount', 'active', 'code')
    search_fields = ('order', 'discount', 'active', 'code')
    list_filter = ('order', 'discount', 'active', 'code')
    ordering = ('order', 'discount', 'active', 'code')
    autocomplete_fields = ('order',)
