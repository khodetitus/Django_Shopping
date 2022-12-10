from django.db import models
from core.models import BaseModel
from customers.models import Customer


# Create your models here


class Category(BaseModel):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    is_sub = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products', default='default.jpg')
    description = models.TextField()
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()

    # is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductFeature(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='features')
    color = models.CharField(max_length=20)
    type = models.CharField(max_length=25)
    material = models.CharField(max_length=25)

    def __str__(self):
        return self.color


class Comment(BaseModel):
    title = models.CharField(max_length=25)
    body = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='c_comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='p_comments')

    def __str__(self):
        return self.title
