from django.views import generic as views
from django.shortcuts import render


class BaseView(views.TemplateView):
    template_name = 'base/base_test_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if self.request.user.is_autenticated:
        #     context['user'] = self.request.user
        #     context['user_id'] = self.request.user.id
        return context


class ShowHomeView(views.TemplateView):
    template_name = 'main/show_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
