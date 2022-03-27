from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('kufarbg_app.main_app.url')),
    path('auth/', include('kufarbg_app.auth_app.url')),
)
