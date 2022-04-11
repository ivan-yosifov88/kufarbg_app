from django.urls import reverse_lazy
from django.views import generic as view

from kufarbg_app.main_app.forms import CreateDestinationForm, DestinationCommentForm
from kufarbg_app.main_app.models import UserTrips, Comments


class CreateDestinationView(view.CreateView):
    form_class = CreateDestinationForm
    template_name = 'main/create_destination.html'
    success_url = reverse_lazy('show home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DestinationsView(view.ListView):
    template_name = 'main/dashboard.html'
    model = UserTrips
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destinations'] = UserTrips.objects.all()
        context['comments'] = Comments.objects.all()
        return context


class DestinationDetailsView(view.DetailView):
    model = UserTrips
    template_name = 'main/destination_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user_id == self.request.user.id
        context['destination'] = self.object

        return context


class MyDestinationDetailsView(view.ListView):
    model = UserTrips
    template_name = 'main/my_destinations.html'
    context_object_name = 'profile'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['destinations'] = UserTrips.objects.all().filter(user=user.id)

        return context


class DestinationCommentView(view.CreateView):
    form_class = DestinationCommentForm
    template_name = 'main/destination_comment.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['destination_id'] = self.kwargs['pk']
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        destination = UserTrips.objects.get(pk=self.kwargs['pk'])
        context["destination"] = destination
        return context
