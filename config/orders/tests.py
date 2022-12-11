from django.test import TestCase
from .models import Order, OrderItem, Coupon
from customers.models import Customer


class OrderModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(user_name="masoud", email="masoudpro2@gmail.com",
                                                phone_number="09120572655", password="123456")
        self.order = Order.objects.create(customer=self.customer, paid=True, discount=10)

    def test_order_creation(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.paid, True)
        self.assertEqual(self.order.discount, 10)

    def test_order_str(self):
        self.assertEqual(str(self.order), "masoud")


class OrderItemModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(user_name="masoud", email="masoudpro2@gmail.com",
                                                phone_number="09120572655", password="123456")
        self.order = Order.objects.create(customer=self.customer, paid=True, discount=10)
        self.order_item = OrderItem.objects.create(product="product", order=self.order, price=1000, quantity=2)

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.product, "product")
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.price, 1000)
        self.assertEqual(self.order_item.quantity, 2)

    def test_order_item_str(self):
        self.assertEqual(str(self.order_item), "product")


class CouponModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(user_name="masoud", email="masoudpro2@gmail.com",
                                                phone_number="09120572655", password="123456")
        self.order = Order.objects.create(customer=self.customer, paid=True, discount=10)
        self.coupon = Coupon.objects.create(order=self.order, discount=10, code="123456",
                                            valid_from="2022-12-09 14:00:00", valid_to="2022-12-15 14:00:00",
                                            active=True)

    def test_coupon_creation(self):
        self.assertEqual(self.coupon.order, self.order)
        self.assertEqual(self.coupon.discount, 10)
        self.assertEqual(self.coupon.code, "123456")
        self.assertEqual(self.coupon.valid_from, "2022-12-09 14:00:00")
        self.assertEqual(self.coupon.valid_to, "2022-12-15 14:00:00")
        self.assertEqual(self.coupon.active, True)

    def test_coupon_str(self):
        self.assertEqual(str(self.coupon), "123456")
