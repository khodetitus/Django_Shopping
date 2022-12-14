from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number']

    def clean_password2(self):
        cd = self.cleaned_data
        password1 = cd.get('password1')
        password2 = cd.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise ValidationError("Password does not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="Raw passwords are not stored, so there is no way to see this user's password, but you can change the password using <a href=\"password/\">this form</a>.")

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number']


class RegisterForm(forms.Form):
    username = forms.CharField(label="",
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "User Name"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}))
    phone_number = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Phone Number"}))
    password1 = forms.CharField(label="",
                                widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Confirm Password"}))

    def clean_username(self):
        username = self.cleaned_data["username"]
        user = User.objects.filter(username=username)
        if user.exists():
            raise ValidationError("This user name is already registered")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email)
        if user.exists():
            raise ValidationError("This email is already registered")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        user = User.objects.filter(phone_number=phone_number)
        if user.exists():
            raise ValidationError("This phone number is already registered")
        return phone_number

    def clean(self):
        cd = super().clean()
        password1 = cd.get("password1")
        password2 = cd.get("password2")

        if password1 and password2:
            if password1 != password2:
                raise ValidationError("Password does not match")


class LoginForm(forms.Form):
    phone_number = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Phone Number"}))
    password = forms.CharField(label="",
                               widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
