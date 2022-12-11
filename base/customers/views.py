from django.shortcuts import render
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request, 'customers/register.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'customers/login.html')


class LogoutView(View):
    def get(self, request):
        return render(request, 'customers/logout.html')
