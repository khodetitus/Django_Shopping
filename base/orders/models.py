from django.db import models
from core.models import BaseModel
from customers.models import User
from products.models import Product


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"User: {self.user} - DateTime Created: {self.created} - Paid: {self.paid} - Discount: {self.discount}"


class OrderItem(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f"Product: {self.product} - Order: {self.order} - Price: {self.price} - Quantity: {self.quantity}"


class Coupon(BaseModel):
    discount = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='use_coupon')
    code = models.CharField(max_length=16, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'

    def __str__(self):
        return f"Order: {self.order} - Discount: {self.discount} - Active: {self.active} - Code: {self.code}"
