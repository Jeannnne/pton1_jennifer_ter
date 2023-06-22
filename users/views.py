from forms import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeView


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm


class CustomLogoutView(LogoutView):
    next_page = 'home'


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    success_url = 'password_reset_done'
    email_template_name = 'registration/password_reset_email.html'
    form_class = CustomPasswordResetForm

