from django.forms import ModelForm, TextInput, Textarea, ChoiceField, Select

from forum.models import Topic, CustomMessage


class CreateTopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'})
        }


class CreateMessageForm(ModelForm):
    class Meta:
        model = CustomMessage
        fields = ['topic', 'content']
        widgets = {
            'content': Textarea(attrs={'class': 'form-control'}),
            'topic': Select(attrs={'class': 'form-control'})
        }
