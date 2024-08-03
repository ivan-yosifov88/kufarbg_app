from django.urls import reverse_lazy
from django.views import generic as view
from django.contrib.auth import mixins as auth_mixins

from kufarbg_app.main_app.forms import DestinationCommentForm
from kufarbg_app.main_app.models import Destinations, Comments




class DestinationCommentView(auth_mixins.LoginRequiredMixin, view.CreateView):
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
        destination = Destinations.objects.get(pk=self.kwargs['pk'])
        context["destination"] = destination
        return context


class AllDestinationComments(view.ListView):
    template_name = 'main/all_comments_destination.html'
    model = Comments
    paginate_by = 1
    ordering = 'created_at'

    def get_queryset(self):
        return Comments.objects.prefetch_related('trip__comments_set').filter(trip_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destination'] = Destinations.objects.get(pk=self.kwargs['pk'])
        return context
