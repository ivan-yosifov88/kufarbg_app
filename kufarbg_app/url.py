from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from kufarbg_app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kufarbg_app.main_app.url')),
    path('auth/', include('kufarbg_app.auth_app.url')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
