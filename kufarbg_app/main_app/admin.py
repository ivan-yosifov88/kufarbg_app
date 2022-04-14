from django.contrib import admin

from kufarbg_app.main_app.models import Destinations, Comments, Likes, SiteOwnerData, HomePageData, AboutUsData


@admin.register(Destinations)
class UserTripsAdmin(admin.ModelAdmin):
    list_display = (
        'country', 'city',
        'description', 'date_of_journey',
        'photo', 'user',
    )


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'trip', 'author',
        'comment', 'created_at',
    )


@admin.register(Likes)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'trip',
    )


@admin.register(SiteOwnerData)
class SiteOwnerDataAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'phone_number',
        'company_name', 'address',
    )


@admin.register(HomePageData)
class ShowHomeViewAdmin(admin.ModelAdmin):
    list_display = (
        'site_images_url', 'good_thoughts',
    )


@admin.register(AboutUsData)
class ShowContactView(admin.ModelAdmin):
    list_display = ('site_owners_description',)
