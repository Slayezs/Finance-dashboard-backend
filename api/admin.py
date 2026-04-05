from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AppUser


class AppUserAdmin(UserAdmin):
    model = AppUser

    list_display = ('username', 'email', 'role', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )


admin.site.register(AppUser, AppUserAdmin)