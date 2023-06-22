from django.contrib.auth.mixins import LoginRequiredMixin

from users.forms import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeView, \
    PasswordResetDoneView, PasswordChangeDoneView, PasswordResetConfirmView, PasswordResetCompleteView


# Create your views here.
class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm


class CustomLogoutView(LogoutView):
    next_page = 'admin console'


# Reset password views
class CustomPasswordResetView(PasswordResetView):
    success_url = 'password_reset/done'
    form_class = CustomPasswordResetForm


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    templates_name = 'registration/password_reset_confirm.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/password_reset_done.html"


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "registration/password_reset_complete.html"


# Change password views
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/password_change.html'
    success_url = 'password_change/done'
    form_class = CustomPasswordChangeForm


class CustomPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'
