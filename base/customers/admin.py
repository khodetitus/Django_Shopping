from django.contrib import admin
from .models import User, Profile, Address, OtpCode
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'username', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    readonly_fields = ('last_login',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'phone_number', 'password')}),
    )
    add_fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'username', 'password1', 'password2')}),
    )
    search_fields = ('email', 'username', 'phone_number')
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(OtpCode)
