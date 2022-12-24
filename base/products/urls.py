from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('product/', views.ProductView.as_view(), name='product'),
    path('', views.LandingView.as_view(), name='landing'),
]
