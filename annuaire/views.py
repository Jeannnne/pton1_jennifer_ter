from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from annuaire.forms import ChangeProfileForm
from users.models import Collaborator


# Create your views here.
class HomeView(ListView):
    model = Collaborator
    paginate_by = 15
    template_name = 'annuaire/home.html'

    def get_queryset(self):
        return Collaborator.objects.all()


def collaborator_view(request):
    if request.method == 'POST':
        form = ChangeProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ChangeProfileForm()
    return render(request, 'annuaire/change_profile.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')