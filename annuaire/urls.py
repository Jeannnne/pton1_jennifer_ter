from django.urls import path
from annuaire import views
from django.conf.urls.static import static

from pton1_jennifer_ter import settings

urlpatterns = [
    path('home', views.HomeView.as_view(), name='annuaire_home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)