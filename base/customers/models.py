from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email']
    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(BaseModel):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cprofile")
    first_name = models.CharField(max_length=50, )
    last_name = models.CharField(max_length=50, )
    CHOICES = [("male", "Male"), ("female", "Female")]
    gender = models.CharField(max_length=10, choices=CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', null=True, blank=True, default='default.jpg')

    def save(self, *args, **kwargs):
        male = 'default/default_male.png'
        female = 'default/default_female.png'
        if not self.image:
            self.image = male if self.gender == 'male' else female
        elif self.image and self.image in [male, female]:
            self.image = male if self.gender == 'male' else female
        super(Profile, self).save(*args, **kwargs)

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

    def __str__(self):
        return self.phone_number
