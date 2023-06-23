from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from annuaire.forms import CreateCollaboratorForm, CollaboratorUpdateForm
from users.models import Collaborator, Service


# Create your views here.
class HomeView(LoginRequiredMixin, ListView):
    model = Collaborator
    template_name = 'annuaire/home.html'
    paginate_by = 2

    def get_queryset(self):
        queryset = Collaborator.objects.all().order_by('service')
        service_id = self.request.GET.get('service_id')

        if service_id:
            queryset = queryset.filter(service__id=service_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        services = Service.objects.all()
        sorted_services = sorted(services, key=lambda x: str(x))

        context['services'] = sorted_services
        return context


class CollaboratorDetailView(LoginRequiredMixin, DetailView):
    model = Collaborator
    template_name = 'annuaire/collaborator_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        collaborator = Collaborator.objects.get(pk=self.kwargs['pk'])

        context['services'] = collaborator.service.all()

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Collaborator
    fields = '__all__'
    exclude = ['date_joined', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions']
    template_name = 'annuaire/profile_update.html'
    form_class = CollaboratorUpdateForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('collaborator-detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.id != self.get_object().id:
            raise Http404("Vous n'êtes pas autorisé à modifier ce profil.")
        return super().dispatch(request, *args, **kwargs)

#
# # Create a new user
# def collaborator_view(request):
#     if request.method == 'POST':
#         form = CreateCollaboratorForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = CreateCollaboratorForm()
#     return render(request, 'annuaire/new_profile.html', {'form': form})
#
#
# def success(request):
#     return HttpResponse('successfully uploaded')
