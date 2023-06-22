from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, DateField
from phonenumber_field.modelfields import PhoneNumberField

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
    service = CharField(blank=True, max_length=100,
                        help_text="Entrez le service du collaborateur "
                                  "(par exemple, RH pour Service des Ressources Humaines)."
                        )

    # Not editable fields
    date_joined = DateField(auto_now_add=True, validators=[validate_date_range])

    def __str__(self):
        return self.username
