from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('product/', views.ProductView.as_view(), name='product'),
    path('', views.LandingView.as_view(), name='landing'),
    path('categories/<slug:slug_category>/', views.CategoryView.as_view(), name='category'),
    path('product/details/<int:product_id>/<slug:slug_product>/', views.ProductDetailView.as_view(),
         name='product-detail'),
]
