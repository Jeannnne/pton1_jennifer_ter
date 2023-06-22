from django.urls import path
from views import *

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),
    path('password_reset', CustomPasswordResetView.as_view(), name='password_reset'),
]