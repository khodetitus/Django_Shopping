from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from django.core.validators import RegexValidator


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator(regex=r'09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}',
                       message='Phone number must be entered in the format: "09xxxxxxxxx". Up to 11 digits allowed.')])
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email']
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"Username: {self.username} - Email: {self.email} - Phone Number : {self.phone_number} - Admin: {self.is_admin}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cprofile")
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    CHOICES = [("male", "MALE"), ("female", "FEMALE")]
    gender = models.CharField(max_length=10, choices=CHOICES, default="male")
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', null=True, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def save(self, *args, **kwargs):
        male = 'default/male.png'
        female = 'default/female.png'
        if not self.image:
            self.image = male if self.gender == 'male' else female
        elif self.image and self.image in [male, female]:
            self.image = male if self.gender == 'male' else female
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f"User: {self.user} - First Name: {self.first_name} - Last Name : {self.last_name} - Gender: {self.gender}"


class Address(BaseModel):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="padress")
    province = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    address1 = models.TextField(max_length=200, null=True, blank=True)
    address2 = models.TextField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator(regex=r'^0[0-9]{2,}[0-9]{7,9}$', message='The Telephone Number invalid',
                       code='invalid_phone_number')], null=True, blank=True)
    postal_code = models.CharField(max_length=10, unique=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f"Profile: {self.profile} - City: {self.city}"


class OtpCode(BaseModel):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Otp Code'
        verbose_name_plural = 'Otp Codes'

    def __str__(self):
        return f"Phone Number: {self.phone_number} - Email: {self.email}"
