from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, DateField
from phonenumber_field.modelfields import PhoneNumberField

from users.validators import validate_french_phone_number, validate_date_range


# Create your models here.

class Collaborator(AbstractUser):
    current_job = CharField(max_length=100)
    phone_number = PhoneNumberField(validators=[validate_french_phone_number])
    email = EmailField(unique=True)
    date_joined = DateField(auto_now_add=True, validators=[validate_date_range])
    date_left = DateField(blank=True, null=True, validators=[validate_date_range])
    current_direction = CharField(blank=True, max_length=100)

    def __str__(self):
        return self.username
