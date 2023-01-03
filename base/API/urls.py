from django.urls import path
from .views import ProfileApiView

app_name = 'API'
urlpatterns = [
    path('profile/<int:user_id>/', ProfileApiView.as_view(), name='profile_api'),
    path('profile/edit/<int:user_id>/', ProfileApiView.as_view(), name='profile_edit_api'),
]
