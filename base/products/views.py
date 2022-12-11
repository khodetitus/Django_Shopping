from django.shortcuts import render
from django.views import View
from .models import Product


class ProductView(View):
    def get(self, request):
        products = Product.objects.filter(is_available=True)
        return render(request, "products/products.html", {"products": products})

    def post(self, request):
        return render(request, "products/products.html")
