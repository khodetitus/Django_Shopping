from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'customers/register.html', {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(["user_name"], cd["email"], cd["phone_number"],
                                            password=["password"])
            user.save()
            messages.success(request, "You Registered Successfully", extra_tags="success")
            return redirect("products:home")


class LoginView(View):
    def get(self, request):
        return render(request, 'customers/login.html')


class LogoutView(View):
    def get(self, request):
        return render(request, 'customers/logout.html')
