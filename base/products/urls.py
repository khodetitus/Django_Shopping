from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('product/', views.ProductView.as_view(), name='product'),
    path('', views.LandingView.as_view(), name='landing'),
    path('categories/<slug:category_slug>', views.CategoryView.as_view(), name='category'),
    path('product-details/<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
]
