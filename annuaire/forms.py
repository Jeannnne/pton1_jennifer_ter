from django import forms
from users.models import Collaborator


class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'current_job',
            'current_direction',
            'service',
            'profile_picture',
            'phone_number',
            'date_left'
        ]
