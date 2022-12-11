from django.contrib import admin
from .models import Order, OrderItem, Coupon
from core.admin import BaseAdmin

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Coupon)
