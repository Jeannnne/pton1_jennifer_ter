from django.urls import path
from annuaire import views


urlpatterns = [
    path('error', views.ErrorView.as_view(), name='error'),

    path('home', views.HomeView.as_view(), name='annuaire_home'),
    path('<int:pk>/details', views.CollaboratorDetailView.as_view(), name='collaborator_detail'),

    path('<int:pk>/update', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('<int:pk>/delete', views.CollaboratorDeleteView.as_view(), name='profile_delete'),



    # path('create_user', views.collaborator_view, name='image_upload'),
    # path('success', views.success, name='success'),
]
