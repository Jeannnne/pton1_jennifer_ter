from django.db import models

from users.models import Collaborator


# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)
    author = models.ForeignKey(Collaborator, on_delete=models.CASCADE)

    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CustomMessage(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Collaborator, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message by {self.author.username} on {self.subject.title}"

