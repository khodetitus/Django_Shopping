from django.contrib import admin
from .models import User, Profile, Address, OtpCode
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from core.admin import BaseAdmin


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['email', 'username', 'phone_number', 'is_admin']
    list_filter = ('is_admin',)
    readonly_fields = ('last_login',)
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'username', 'password')}),
        ('permission',
         {'fields': ('is_active', 'is_admin', 'last_login', 'groups', 'user_permissions', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'username', 'password1', 'password2')}),
    )
    search_fields = ('email', 'username', 'phone_number')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuer'].disabled = True
        return form


admin.site.register(User, UserAdmin)


@admin.register(Profile)
class ProfileAdmin(BaseAdmin):
    list_display = ('user', 'first_name', 'last_name', 'gender')
    search_fields = ('user', 'first_name', 'last_name', 'gender')
    list_filter = ('user',)
    ordering = ('user',)
    autocomplete_fields = ('user',)


@admin.register(Address)
class AddressAdmin(BaseAdmin):
    list_display = ('profile', 'province', 'city', 'tel')
    search_fields = ('profile', 'city')
    list_filter = ('profile',)
    ordering = ('profile',)
    autocomplete_fields = ('profile',)


@admin.register(OtpCode)
class OtpCodeAdmin(BaseAdmin):
    list_display = ('phone_number', 'created', 'email')
    search_fields = ('phone_number', 'created', 'email')
    list_filter = ('phone_number', 'created', 'email')
    ordering = ('phone_number',)
