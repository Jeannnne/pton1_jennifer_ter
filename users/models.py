from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, DateField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

from users.utils import download_default_profile_image
from users.validators import validate_date_range


# Create your models here.

class Collaborator(AbstractUser):
    # Not required fields
    email = EmailField(blank=True)
    date_left = DateField(
        blank=True,
        null=True,
        validators=[validate_date_range]
    )
    current_direction = CharField(
        blank=True,
        max_length=100,
        help_text="Entrez la direction actuelle du collaborateur "
                  "(par exemple, Direction des Systèmes d'Information)."
    )

    profile_picture = models.ImageField(
        upload_to='default_images/',
        default=download_default_profile_image
    )

    # Required fields
    service = models.ManyToManyField('Service', related_name='collaborators')
    current_job = CharField(max_length=100)
    phone_number = PhoneNumberField(
        region='FR',
        help_text="Entrez un numéro de téléphone au format français "
                  "(par exemple, 0612345678)."
    )

    # Not editable fields
    date_joined = DateField(auto_now_add=True, validators=[validate_date_range])

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.profile_picture.name == 'default_profile_image.jpg':
            self.profile_picture.name = self.profile_picture.field.upload_to
        super().save(*args, **kwargs)


class Service(models.Model):
    parent_group = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        if self.parent_group is None:
            return self.name
        return self.parent_group.__str__() + '/' + self.name
