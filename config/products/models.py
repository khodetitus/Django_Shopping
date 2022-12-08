from django.db import models
from ..core.models import BaseModel
from ..customers.models import Customer


# Create your models here
class Product(BaseModel):
    category = models.ManyToManyField('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products')
    description = models.TextField()
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()

    # is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    sub_category = models.ManyToManyField("self", blank=True, null=True, on_delete=models.CASCADE)
    is_sub = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductFeature(BaseModel):
    color = models.CharField(max_length=20)
    type = models.CharField(max_length=25)
    material = models.CharField(max_length=25)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.color


class Comment(BaseModel):
    title = models.CharField(max_length=25)
    body = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
