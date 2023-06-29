from django.urls import path

from forum import views

urlpatterns = [
    path('subjects/', views.SubjectListView.as_view(), name='forum_home'),
    path('subjects/add/', views.SubjectCreateView.as_view(), name='subject_create'),
    path('subjects/<int:pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('subjects/<int:pk>/reply/', views.MessageCreateView.as_view(), name='message_create'),
]