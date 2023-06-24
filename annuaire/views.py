from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, DeleteView

from annuaire.forms import CollaboratorUpdateForm
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
    template_name = 'annuaire/profile_update.html'
    form_class = CollaboratorUpdateForm
    context_object_name = 'collaborator'

    def dispatch(self, request, *args, **kwargs):
        collaborator_id = kwargs['pk']

        if self.request.user.id != collaborator_id:
            return redirect('error')

        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('collaborator_detail', kwargs={'pk': self.object.pk})


class CollaboratorDeleteView(UserPassesTestMixin, DeleteView):
    model = Collaborator
    template_name = 'annuaire/collaborator_delete.html'
    success_url = reverse_lazy('annuaire_home')

    def test_func(self):
        collaborator = self.get_object()
        return collaborator.can_be_deleted_by(self.request.user)

    def handle_no_permission(self):
        return redirect('error')


class ErrorView(LoginRequiredMixin, TemplateView):
    template_name = 'annuaire/error.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Vous n'avez pas les authorisations nécessaires pour accéder à cette page."
        return context


class FormerCollaboratorsView(LoginRequiredMixin, ListView):
    model = Collaborator
    template_name = 'annuaire/former_collaborators.html'
    paginate_by = 2
    context_object_name = 'former_collaborators'

    def get_queryset(self):
        queryset = Collaborator.objects.filter(date_left__lte=timezone.now().date())
        service_id = self.request.GET.get('service_id')

        if service_id:
            queryset = queryset.filter(service__id=service_id)

        return queryset


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
