from django.shortcuts import render
from django.views import View
from .models import Product, Category


class ProductView(View):
    def get(self, request):
        products = Product.objects.get_active_list().filter(is_available=True)
        return render(request, "products/products.html", {"products": products})


class LandingView(View):
    def get(self, request):
        return render(request, "products/landing.html")


class CategoryView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.get_active_list()
        if category_slug:
            category = Category.objects.get_active_list().filter(slug=category_slug)
            products = products.filter(category__in=category)
        return render(request, 'products/products.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, slug):
        product = Product.objects.get_active_list().get(slug=slug)
        return render(request, "products/product_detail.html", {"product": product})
