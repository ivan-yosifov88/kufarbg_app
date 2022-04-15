from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views import generic as view
from django.contrib.auth import mixins as auth_mixins
from kufarbg_app.main_app.forms import CreateDestinationForm, DeleteDestinationForm, EditDestinationForm
from kufarbg_app.main_app.models import Destinations, Comments, Likes


class CreateDestinationView(auth_mixins.LoginRequiredMixin, view.CreateView):
    form_class = CreateDestinationForm
    template_name = 'main/create_destination.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditDestinationView(auth_mixins.LoginRequiredMixin, view.UpdateView):
    model = Destinations
    form_class = EditDestinationForm
    template_name = 'main/edit_destination.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        handler = super(EditDestinationView, self).dispatch(request, *args, **kwargs)
        try:
            owner_user = self.object.user
        except AttributeError:
            return HttpResponseForbidden("403 Forbidden")
        if owner_user != request.user:
            return HttpResponseForbidden("403 Forbidden")
        return handler


class DeleteDestinationView(auth_mixins.LoginRequiredMixin, view.DeleteView):
    model = Destinations
    form_class = DeleteDestinationForm
    template_name = 'main/delete_destination.html'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        handler = super(DeleteDestinationView, self).dispatch(request, *args, **kwargs)
        try:
            owner_user = self.object.user
        except AttributeError:
            return HttpResponseForbidden("403 Forbidden")
        if owner_user != request.user:
            return HttpResponseForbidden("403 Forbidden")
        return handler


class DestinationsView(view.ListView):
    template_name = 'main/dashboard.html'
    model = Destinations
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destinations'] = Destinations.objects.all()
        context['comments'] = Comments.objects.all()
        context['likes'] = Likes.objects.all()
        return context


class DestinationDetailsView(view.DetailView):
    model = Destinations
    template_name = 'main/destination_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user_id == self.request.user.id
        context['is_authenticated'] = self.request.user.is_authenticated
        context['destination'] = self.object
        context['has_liked'] = Likes.objects.prefetch_related('trip__likes_set').filter(
            user_id=self.request.user.id).filter(trip_id=self.object.pk)
        comments = Comments.objects.prefetch_related('trip__comments_set').filter(trip_id=self.object.pk)
        context['comments'] = comments[:3]
        context['comments_count'] = len(comments)
        return context


class MyDestinationDetailsView(auth_mixins.LoginRequiredMixin, view.ListView):
    model = Destinations
    template_name = 'main/my_destinations.html'
    context_object_name = 'profile'
    paginate_by = 3

    def get_queryset(self):
        return Destinations.objects.all().filter(user=self.request.user.id)
