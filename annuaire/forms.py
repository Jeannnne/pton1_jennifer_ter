from django import forms
from users.models import Collaborator


class CreateCollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions']


class CollaboratorUpdateForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields.keys())
        self.fields['date_left'].widget.attrs['readonly'] = True
