from users.forms import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeView, \
    PasswordResetDoneView, PasswordChangeDoneView


# Create your views here.
class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm


class CustomLogoutView(LogoutView):
    next_page = 'admin console'


class CustomPasswordResetView(PasswordResetView):
    success_url = 'password_reset_done'
    form_class = CustomPasswordResetForm


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/password_reset_done.html"


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = 'password_change_done'
    form_class = CustomPasswordChangeForm


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'
