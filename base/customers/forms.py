from django import forms
from .models import Customer


class RegisterForm(forms.Form):
    user_name = forms.CharField(label="",
                                widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "User Name"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}))
    phone_number = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Phone Number"}))
    password = forms.CharField(label="",
                               widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))

    def clean_email(self):
        email = self.cleaned_data["email"]
        customer = Customer.objects.filter(email=email)
        if customer.exists():
            raise forms.ValidationError("This email is already registered")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        customer = Customer.objects.filter(phone_number=phone_number)
        if customer.exists():
            raise forms.ValidationError("This phone number is already registered")
        return phone_number

# class LoginForm(forms.Form):
#     email = forms.EmailField()
#     password = forms.CharField()
