from django.urls import path

from kufarbg_app.auth_app.views import UserLoginView, UserRegisterView, EditProfileView, DeleteProfileView, \
    ChangePasswordView, UserDetailsView, UserLogoutView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='create profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile_details/<int:pk>/', UserDetailsView.as_view(), name='profile details'),
    path('edit_profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('delete_profile/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),
    path('change_pass/<int:pk>/', ChangePasswordView.as_view(), name='change pass'),
)
