from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView

from forum.forms import CreateSubjectForm, CreateMessageForm
from forum.models import Subject, CustomMessage


# Create your views here.
class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'forum/home.html'
    context_object_name = 'subjects'


class SubjectDetailView(LoginRequiredMixin, DetailView):
    model = Subject


class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = CreateSubjectForm
    template_name = 'forum/add_topic.html'
    success_url = '/forum/subjects/'

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author

        return super().form_valid(form)


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = CustomMessage
    form_class = CreateMessageForm
    template_name = 'forum/add_message.html'
    success_url = '/forum/subjects/'

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        form.instance.subject_id = self.kwargs['pk']

        return super().form_valid(form)
