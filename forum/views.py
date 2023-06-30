from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView

from forum.forms import CreateSubjectForm, CreateMessageForm
from forum.models import Subject, CustomMessage


# Create your views here.
class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'forum/home.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        return Subject.objects.all().order_by('-last_updated_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        ordered_messages = CustomMessage.objects.all().order_by('-created_at')
        subjects = Subject.objects.all().order_by('-created_at')

        context_messages = []

        for subject in subjects:
            subject_messages = ordered_messages.filter(subject_id=subject.id).order_by('-created_at')
            tuple = (subject.id, subject_messages.count(), subject_messages.first())

            context_messages.append(tuple)

        context['context_messages'] = context_messages

        return context


class SubjectDetailView(LoginRequiredMixin, DetailView):
    model = Subject

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages = CustomMessage.objects.filter(subject_id=self.kwargs['pk']).order_by('created_at')
        context['messages'] = messages

        return context


class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = CreateSubjectForm
    template_name = 'forum/add_subject.html'
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = Subject.objects.get(id=self.kwargs['pk'])
        context['subject'] = subject

        return context

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author

        # Update the date of the last message
        subject = Subject.objects.get(id=self.kwargs['pk'])
        subject.save()

        form.instance.subject = subject

        return super().form_valid(form)

    def get_success_url(self):
        subject_id = self.kwargs['pk']
        return reverse('subject_detail', kwargs={'pk': subject_id})
