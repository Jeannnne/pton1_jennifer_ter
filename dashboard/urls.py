from django.urls import path

from dashboard import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='dashboard_home')
]
