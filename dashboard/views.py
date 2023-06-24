import requests
import tweepy
from django.views.generic import TemplateView

from pton1_jennifer_ter import settings


# Create your views here.
class HomeView(TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        return context


