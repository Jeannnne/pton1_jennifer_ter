from django.views.generic import ListView

from users.models import Collaborator


# Create your views here.
class HomeView(ListView):
    model = Collaborator
    paginate_by = 15
    template_name = 'annuaire/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["collaborators"] = Collaborator.objects.all()
        
        return context
