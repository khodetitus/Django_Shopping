from django.shortcuts import render
from django.views import View
from .models import Product, Category


class ProductView(View):
    def get(self, request):
        products = Product.objects.filter(is_available=True)
        return render(request, "products/products.html", {"products": products})


class LandingView(View):
    def get(self, request):
        return render(request, "products/landing.html")


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.filter(is_sub=False)
        return render(request, "products/category.html", {"category": categories})


class ProductDetailView(View):
    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        return render(request, "products/product_detail.html", {"product": product})
