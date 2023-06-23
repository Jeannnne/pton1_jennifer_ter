from django import forms
from users.models import Collaborator


class CreateCollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = '__all__'
        exclude = ['date_joined', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions']

class CollaboratorUpdateForm:
    class Meta:
        model = Collaborator
        fields = '__all__'
        exclude = ['date_joined', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions']