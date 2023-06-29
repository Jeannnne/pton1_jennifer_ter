from django.db import models

from users.models import Collaborator


# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_open = models.BooleanField(default=True)
    author = models.ForeignKey(Collaborator, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class CustomMessage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Collaborator, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

