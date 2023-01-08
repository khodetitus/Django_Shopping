from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileView, AboutView, ContactView, PasswordResetView

app_name = 'customers'

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
    path('reset-password/', PasswordResetView.as_view(), name='reset_password'),
    # path('verify/', OtpCodeView.as_view(), name='verify'),
]
