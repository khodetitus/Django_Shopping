from django.urls import path
from .views import ProfileApiView, ProfileEditApiView, ProductListApiView, CategoryListApiView, ProductDetailApiView

app_name = 'API'
urlpatterns = [
    path('profile/<int:user_id>/', ProfileApiView.as_view(), name='profile_api'),
    path('profile/edit/<int:user_id>/', ProfileEditApiView.as_view(), name='profile_edit_api'),
    path('product/list/', ProductListApiView.as_view(), name='product_list_api'),
    path('category/list/', CategoryListApiView.as_view(), name='category_list_api'),
    path('product/detail/<slug:slug_product>/', ProductDetailApiView.as_view(), name='product_detail_api'),
]
