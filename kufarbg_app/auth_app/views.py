import profile

from django.contrib.auth import views as auth_views, get_user_model, login
from django.views import generic as views
from django.shortcuts import render
from django.urls import reverse_lazy

from kufarbg_app.auth_app.forms import UserRegistrationForm, EditProfileForm
from kufarbg_app.auth_app.models import Profile


class UserRegisterView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'auth_app/create_profile.html'
    success_url = reverse_lazy('show home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserDetailsView(views.DetailView):
    model = Profile
    template_name = 'auth_app/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # tab data here


        return context


class EditProfileView(views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'auth_app/edit_profile.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('show home')


class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = 'auth_app/delete_profile.html'
    context_object_name = 'profile'


class UserLoginView(auth_views.LoginView):
    template_name = 'auth_app/login.html'
    success_url = reverse_lazy('show home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ChangePasswordView(auth_views.PasswordChangeView):
    template_name = 'auth_app/change_password.html'
    success_url = reverse_lazy('show home')
