from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, DateField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

from users.validators import validate_date_range


# Create your models here.

class Collaborator(AbstractUser):
    # Not required fields
    email = EmailField(blank=True)
    date_left = DateField(blank=True,
                          null=True,
                          validators=[validate_date_range]
                          )
    current_direction = CharField(blank=True, max_length=100,
                                  help_text="Entrez la direction actuelle du collaborateur "
                                            "(par exemple, Direction des Systèmes d'Information)."
                                  )

    # Required fields
    current_job = CharField(blank=True, max_length=100)
    phone_number = PhoneNumberField(blank=True, region='FR',
                                    help_text="Entrez un numéro de téléphone au format français "
                                              "(par exemple, 0612345678)."
                                    )
    service = models.ManyToManyField('Service', related_name='collaborators')

    # Not editable fields
    date_joined = DateField(auto_now_add=True, validators=[validate_date_range])

    def __str__(self):
        return self.username


class Service(models.Model):
    parent_group = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name
