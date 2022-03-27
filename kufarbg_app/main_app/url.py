from django.urls import path

from kufarbg_app.main_app.views import ShowHomeView

urlpatterns = (
    path('', ShowHomeView.as_view(), name='show home'),
)
