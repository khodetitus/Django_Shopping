from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone


class BaseAdmin(admin.ModelAdmin):
    def logical_deleter(self, request, queryset):
        queryset.update(deleted_at=timezone.now())
        queryset.update(is_deleted=True)
        queryset.update(is_active=False)

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)

    def activate(self, request, queryset):
        queryset.update(is_active=True)

    actions = ['logical_deleter', 'deactivate', 'activate']
