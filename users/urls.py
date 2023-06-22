from django.urls import path
from users.views import *

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),

    path('password_reset', CustomPasswordResetView.as_view(), name='password_reset'),
    path('passowrd_reset/done', CustomPasswordResetDoneView.as_view(0), name='password_reset_done'),

    path('password_change', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
]