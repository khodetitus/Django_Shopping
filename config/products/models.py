from django.db import models
from ..core.models import BaseModel


# Create your models here
class Product(BaseModel):
    name = models.CharField(max_length=25)
