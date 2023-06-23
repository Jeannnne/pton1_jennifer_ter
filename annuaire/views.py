from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView

from annuaire.forms import ChangeProfileForm
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


# Create a new user
def collaborator_view(request):
    if request.method == 'POST':
        form = ChangeProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ChangeProfileForm()
    return render(request, 'annuaire/new_profile.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


class CollaboratorDetailView(LoginRequiredMixin, DetailView):
    model = Collaborator
    template_name = 'annuaire/collaborator_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        collaborator = Collaborator.objects.get(pk=self.kwargs['pk'])

        context['services'] = collaborator.service.all()

        return context
