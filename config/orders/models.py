from django.db import models
from core.models import BaseModel
from customers.models import Customer
from products.models import Product


# Create your models here.

class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)


class OrderItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)


class Coupon(BaseModel):
    discount = models.IntegerField()
    code = models.CharField(max_length=16)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='use_coupon')
