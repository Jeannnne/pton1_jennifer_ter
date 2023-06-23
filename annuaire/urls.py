from django.urls import path
from annuaire import views


urlpatterns = [
    path('home', views.HomeView.as_view(), name='annuaire_home'),
    path('create_user', views.collaborator_view, name='image_upload'),
    path('success', views.success, name='success'),
]
