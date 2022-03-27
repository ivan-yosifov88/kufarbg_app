from django.contrib import admin

from kufarbg_app.auth_app.models import Profile, AppUser


@admin.register(AppUser)
class UsersAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
