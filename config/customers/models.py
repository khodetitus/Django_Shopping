from django.db import models
from core.models import BaseModel


class Customer(BaseModel):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name


class Profile(BaseModel):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="cprofile")
    first_name = models.CharField(max_length=50, )
    last_name = models.CharField(max_length=50, )
    CHOICES = [("male", "Male"), ("female", "Female")]
    gender = models.CharField(max_length=10, choices=CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', null=True, blank=True, default='default.jpg')

    def __str__(self):
        return self.first_name


class Address(BaseModel):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="padress")
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=11)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.city


class OtpCode(BaseModel):
    phone_number = models.CharField(max_length=11)
    code = models.PositiveIntegerField()
    email = models.EmailField(null=True, blank=True)
