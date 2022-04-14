import datetime

from django.urls import reverse_lazy
from django.views import generic as views

from kufarbg_app.main_app.forms import ContactForm
from kufarbg_app.main_app.models.generic import HomePageData, SiteOwnerData


class BaseView(views.TemplateView):
    template_name = 'base/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShowHomeView(views.TemplateView):
    template_name = 'main/show_home.html'

    def get_context_data(self, **kwargs):
        day = datetime.datetime.now().day
        context = super().get_context_data(**kwargs)
        home_data = HomePageData.objects.filter(pk=day)
        if home_data:
            context['photos'] = home_data[0]
            context['thoughts'] = home_data[1]
        else:
            context['photos'] = HomePageData.DEFAULT_IMAGE_URL
            context['thoughts'] = HomePageData.DEFAULT_THOUGHTS
        context['user'] = self.request.user
        return context


class ShowContactView(views.FormView):
    form_class = ContactForm
    template_name = 'main/site_owner/contact_us.html'
    success_url = reverse_lazy('show_home')

    def get_context_data(self, **kwargs):
        owner_data = SiteOwnerData.objects.all()
        # SiteOwnerData.objects.filter(pk=1).exists()
        context = super().get_context_data(**kwargs)
        if owner_data:
            context['owner_data'] = owner_data[0]
        return context


class ShowAboutView(views.TemplateView):
    template_name = 'main/site_owner/about_us.html'
