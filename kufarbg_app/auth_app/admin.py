from django.contrib import admin

from kufarbg_app.auth_app.models import Profile, AppUser


@admin.register(AppUser)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'date_joined',
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name',
        'phone_number', 'date_of_birth',
        'image_url', 'gender',
        'user',
    )
