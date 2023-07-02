from django.urls import path

from forum import views

urlpatterns = [
    path('', views.SubjectListView.as_view(), name='forum_home'),
    path('<int:pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),

    path('add/', views.SubjectCreateView.as_view(), name='subject_create'),
    path('<int:pk>/reply/', views.MessageCreateView.as_view(), name='message_create'),
]