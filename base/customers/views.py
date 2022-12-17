from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(View):
    class_form = RegisterForm
    template_name = 'customers/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("products:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd["username"], email=cd["email"],
                                            phone_number=cd["phone_number"], password=cd["password"])
            user.save()
            messages.success(request, "You Registered Successfully", "success")
            return redirect("products:home")

        return render(request, self.template_name, {"form": form})


class LoginView(View):
    form_class = LoginForm
    template_name = 'customers/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("products:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number=cd["phone_number"], password=cd["password"])

            if user is not None:
                login(request, user)
                messages.success(request, "You Logged In Successfully", "success")
                return redirect("products:home")
            messages.error(request, "Invalid User Name or Password", "danger")
        return render(request, self.template_name, {"form": form})


class LogoutView(LoginRequiredMixin, View):
    login_url = "customers:login"

    def get(self, request):
        logout(request)
        messages.success(request, "You Logged Out Successfully", "success")
        return redirect("products:home")


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, "customers/profile.html", {"user": user})
