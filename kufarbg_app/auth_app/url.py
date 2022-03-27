from django.urls import path

from kufarbg_app.auth_app.views import UserLoginView, UserRegisterView, EditProfileView, DeleteProfileView, \
    ChangePasswordView, UserDetailsView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='create profile'),
    path('profile_details/<int:pk>/', UserDetailsView.as_view(), name='profile details'),
    path('edit_profile/', EditProfileView.as_view(), name='edit profile'),
    path('delete_profile/', DeleteProfileView.as_view(), name='delete profile'),
    path('change_pass/', ChangePasswordView.as_view(), name='change pass'),
)
