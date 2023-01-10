from django.shortcuts import render, get_list_or_404,get_object_or_404
from django.views import View
from .models import Product, Category
from orders.forms import CartAddForm


class ProductView(View):
    def get(self, request):
        products = get_list_or_404(Product, is_available=True, is_active=True, is_deleted=False)
        return render(request, "products/products.html", {"products": products})


class LandingView(View):
    def get(self, request):
        return render(request, "products/landing.html")


class CategoryView(View):
    def get(self, request, slug_category):
        products = Product.objects.get_active_list()
        if slug_category:
            category = get_list_or_404(Category, slug=slug_category, is_active=True, is_deleted=False)
            products = get_list_or_404(products, category__in=category)
        return render(request, 'products/products.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, product_id):
        form = CartAddForm
        product = get_object_or_404(Product, id=product_id, is_active=True, is_deleted=False)

        return render(request, "products/product_detail.html", {"product": product, "form": form})
