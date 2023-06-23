from django import forms
from users.models import Collaborator


class CreateCollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = '__all__'
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions']


class CollaboratorUpdateForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = '__all__'
        exclude = ['password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'is_active', 'is_staff']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_left'].widget.attrs['readonly'] = True
