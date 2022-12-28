# import random
# from core.utils import send_otp_code
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm, ProfileForm, OtpCodeForm
from .models import User, Profile, Address, OtpCode
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'customers/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # random_code = random.randint(1000, 9999)
            # send_otp_code(form.cleaned_data['phone_number'], random_code)
            # OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd["username"], email=cd["email"],
                                            phone_number=cd["phone_number"], password=cd["password1"])
            user.save()
            messages.success(request, "The code has been sent to your phone", "success")
            # print(random_code)
            return redirect("customers:verify")
        return render(request, self.template_name, {"form": form})


# class OtpCodeView(View):
    # form_class = OtpCodeForm
    #
    # def get(self, request):
    #     form = self.form_class()
    #     return render(request, 'customers/otp-code.html', {'form': form})
    #
    # def post(self, request):
    #     user_session = request.session['user_registration_info']
    #     code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         if cd['code'] == code_instance.code:
    #             User.objects.create_user(username=user_session['username'], email=user_session['email'],
    #                                      phone_number=user_session['phone_number'], password=user_session['password'])
    #             code_instance.delete()
    #             messages.success(request, 'Registered Successfully', 'success')
    #             return redirect('home:home')
    #         messages.error(request, 'The entered code is not correct', 'danger')
    #         return redirect('customers:verify')
    #     return redirect('products:landing')


class LoginView(View):
    form_class = LoginForm
    template_name = 'customers/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("products:landing")
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
                return redirect("products:landing")
            messages.error(request, "Invalid User Name or Password", "danger")
        return render(request, self.template_name, {"form": form})


class LogoutView(LoginRequiredMixin, View):
    login_url = "customers:login"

    def get(self, request):
        logout(request)
        messages.success(request, "You Logged Out Successfully", "success")
        return redirect("products:landing")


class ProfileView(LoginRequiredMixin, View):
    form_class = ProfileForm
    template_name = 'customers/profile.html'

    def setup(self, request, *args, **kwargs):
        self.user = User.objects.get(id=kwargs["user_id"])
        self.profile = Profile.objects.get(user=self.user)
        self.address = Address.objects.get(profile=self.profile)
        return super().setup(request, *args, **kwargs)

    def get(self, request, user_id):
        profile = self.profile
        form = self.form_class(instance=self.address,
                               initial={"first_name": profile.first_name, "last_name": profile.last_name,
                                        "gender": profile.gender, "birth_date": profile.birth_date,
                                        "image": profile.image})
        return render(request, self.template_name, {"form": form, "image": profile.image})

    def post(self, request, user_id):
        form = self.form_class(request.POST, instance=self.address, files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            self.profile.first_name = cd["first_name"]
            self.profile.last_name = cd["last_name"]
            self.profile.gender = cd["gender"]
            self.profile.birth_date = cd["birth_date"]
            self.profile.image = cd["image"]
            self.profile.save()
            form.save()
            messages.success(request, "Your Profile Updated Successfully", "success")
            return redirect("customers:profile", user_id=user_id)
        messages.error(request, "Error Please Try Again!", "danger")
        return render(request, self.template_name, {"form": form})


class AboutView(View):
    def get(self, request):
        return render(request, "customers/about.html")


class ContactView(View):
    def get(self, request):
        return render(request, "customers/contact.html")
