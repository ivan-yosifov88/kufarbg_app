from django.contrib.auth import views as auth_views, login, logout
from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponseForbidden, Http404
from django.views import generic as views
from django.urls import reverse_lazy
from kufarbg_app.auth_app.forms import UserRegistrationForm, EditProfileForm, DeleteProfileForm, LoginForm, \
    ChangePasswordForm
from kufarbg_app.auth_app.models import Profile, AppUser


class UserRegisterView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'auth_app/create_profile.html'
    success_url = reverse_lazy('show home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLogoutView(auth_views.LogoutView):
    redirect_field_name = reverse_lazy('show home')


class UserDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Profile
    template_name = 'auth_app/profile_details.html'
    context_object_name = 'profile'

    def dispatch(self, request, *args, **kwargs):
        handler = super(UserDetailsView, self).dispatch(request, *args, **kwargs)
        if self.object.user != request.user:
            return HttpResponseForbidden("403 Forbidden Can't touch this.")
        return handler

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user_id == self.request.user.id
        return context


class EditProfileView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'auth_app/edit_profile.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('show home')

    def dispatch(self, request, *args, **kwargs):
        handler = super(EditProfileView, self).dispatch(request, *args, **kwargs)
        if self.object.user != request.user:
            return HttpResponseForbidden("403 Forbidden Can't touch this.")
        return handler


class DeleteProfileView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Profile
    form_class = DeleteProfileForm
    template_name = 'auth_app/delete_profile.html'
    success_url = reverse_lazy('show home')

    def dispatch(self, request, *args, **kwargs):
        handler = super(DeleteProfileView, self).dispatch(request, *args, **kwargs)
        if self.object.user != request.user:
            return HttpResponseForbidden("403 Forbidden Can't touch this.")
        return handler

    def form_valid(self, form_class):
        user = AppUser.objects.get(id=self.object.user_id)
        result = super().form_valid(form_class)
        user.delete()
        logout(self.request)
        return result


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'auth_app/login.html'
    success_url = reverse_lazy('show home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ChangePasswordView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'auth_app/change_password.html'
    success_url = reverse_lazy('show home')
