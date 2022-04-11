import datetime

from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from kufarbg_app.main_app.forms import ContactForm
from kufarbg_app.main_app.models.generic import HomePagePhotos, HomePageThoughts, SiteOwnerData


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
        photos = HomePagePhotos.objects.filter(pk=day)
        thoughts = HomePageThoughts.objects.filter(pk=day)
        if photos:
            context['photos'] = photos[0].site_images_url
        else:
            # TODO Add default image
            context['photos'] = HomePagePhotos.DEFAULT_IMAGE_URL
        if thoughts:
            context['thoughts'] = thoughts[0].good_thoughts
        else:
            context['thoughts'] = HomePageThoughts.DEFAULT_THOUGHTS
        context['user'] = self.request.user
        return context


class ShowContactView(views.FormView):
    form_class = ContactForm
    template_name = 'main/contact_us.html'
    success_url = reverse_lazy('show_home')

    def get_context_data(self, **kwargs):
        owner_data = SiteOwnerData.objects.all()
        # SiteOwnerData.objects.filter(pk=1).exists()
        context = super().get_context_data(**kwargs)
        if owner_data:
            context['owner_data'] = owner_data[0]
        return context
