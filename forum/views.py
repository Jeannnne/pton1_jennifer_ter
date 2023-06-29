from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from forum.models import Topic


# Create your views here.
class AddTopicView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'description']
