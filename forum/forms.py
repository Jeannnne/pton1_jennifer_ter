from django.forms import ModelForm, TextInput, Textarea, Select, CharField

from forum.models import Subject, CustomMessage


class CreateSubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'})
        }


class CreateMessageForm(ModelForm):
    class Meta:
        model = CustomMessage
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'class': 'form-control'})
        }
