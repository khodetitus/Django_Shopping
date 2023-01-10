from django.db import models
from core.models import BaseModel
from customers.models import User
from django.urls import reverse


class Category(BaseModel):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    is_sub = models.BooleanField(default=False)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return f"Name: {self.name} - Sub Category: {self.sub_category}"


class Product(BaseModel):
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products', default='default/default_product.png', null=True, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def save(self, *args, **kwargs):
        if self.stock > 0:
            self.is_available = True
        else:
            self.is_available = False
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product-detail', args=[self.id])


class ProductFeature(BaseModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='features')
    color = models.CharField(max_length=20)
    type = models.CharField(max_length=25)
    material = models.CharField(max_length=25)

    class Meta:
        verbose_name = "Product Feature"
        verbose_name_plural = "Product Features"

    def __str__(self):
        return f"Product: {self.product} - Color: {self.color} - Type: {self.type} - Material: {self.material}"


class Comment(BaseModel):
    title = models.CharField(max_length=25)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='c_comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='p_comments')

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"User: {self.user} - Product: {self.product}"
