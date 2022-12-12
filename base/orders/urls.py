from django.urls import path
from .views import OrderView

app_name = 'orders'
urlpatterns = [
    path('orders/', OrderView.as_view(), name="order")
]
