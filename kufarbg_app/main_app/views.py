from django.views import generic as views
from django.shortcuts import render


class ShowHomeView(views.TemplateView):
    template_name = 'main/show_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
