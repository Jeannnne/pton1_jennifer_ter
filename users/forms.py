from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, UserCreationForm
from django import forms

from users.models import Service, Collaborator


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
    )


class CustomPasswordChangeForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="Confirm new password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )


class CreateCollaboratorForm(UserCreationForm):
    email = forms.EmailField(required=False)
    service = forms.ModelMultipleChoiceField(queryset=Service.objects.all())
    current_job = forms.CharField(max_length=100)
    phone_number = forms.CharField()

    class Meta:
        model = Collaborator
        fields = ('username', 'email', 'password1', 'password2', 'service', 'current_job', 'phone_number')
