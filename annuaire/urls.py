from django.urls import path
from annuaire import views


urlpatterns = [
    path('home', views.HomeView.as_view(), name='annuaire_home'),
    path('<int:pk>/details', views.CollaboratorDetailView.as_view(), name='collaborator_detail'),
    path('<int:pk>/update', views.ProfileUpdateView.as_view(), name='profile_update'),

    # path('create_user', views.collaborator_view, name='image_upload'),
    # path('success', views.success, name='success'),
]
