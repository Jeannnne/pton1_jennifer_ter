from io import BytesIO

import requests
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractUser
from django.core.files import File
from django.db.models import CharField, EmailField, DateTimeField
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

from pton1_jennifer_ter import settings
from users.validators import validate_date_range


# Create your models here.

class Collaborator(AbstractUser):
    # Not required fields
    email = EmailField(blank=True)
    date_left = DateTimeField(
        blank=True,
        null=True,
        validators=[validate_date_range]
    )

    profile_picture = models.ImageField(
        upload_to=settings.PROFILE_PICTURE_DIR_NAME + '/',
        blank=True,
        null=True,
    )

    # Required fields
    service = models.ManyToManyField(
        'Service',
        related_name='collaborators',
        help_text="Selectionnez le service du collaborateur.S'il n'est pas disponible veuillez le créer."
    )
    current_job = CharField(max_length=100)
    phone_number = PhoneNumberField(
        region='FR',
        help_text="Entrez un numéro de téléphone au format français "
                  "(par exemple, 0612345678)."
    )

    # Not editable fields
    company_date_joined = DateTimeField(
        auto_now_add=True,
        validators=[validate_date_range]
    )

    api_key = models.CharField(max_length=40, blank=True, null=True)
    api_secret = models.CharField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.profile_picture:
            response = requests.get(settings.DEFAULT_IMAGE_LINK, stream=True)
            response.raise_for_status()

            if response.ok:
                image_file = BytesIO(response.content)
                self.profile_picture.save(settings.DEFAULT_IMAGE_NAME, File(image_file))

            else:
                print("Error while downloading default image")

        super().save(*args, **kwargs)

    def can_be_deleted_by(self, user):
        return user.is_superuser

    def has_valid_api_secret(self, secret_key: str) -> bool:
        return check_password(secret_key, self.api_secret)


class Service(models.Model):
    parent_group = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(
        unique=True,
        max_length=100
    )

    def __str__(self):
        if self.parent_group is None:
            return self.name
        return self.parent_group.__str__() + '/' + self.name
