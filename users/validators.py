from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import re


def validate_french_phone_number(value):
    pattern = r'^(?:\+33|0)[1-9]\d{8}$'
    if not re.match(pattern, value):
        raise ValidationError("Le numéro de téléphone doit être au format français.")


def validate_date_range(value):
    # Year, month, day
    min_date = date(1970, 1, 1)
    max_date = date(2050, 12, 31)

    if value < min_date or value > max_date:
        raise ValidationError(
            _("La date doit être comprise entre {min_date} et {max_date}."
              .format(min_date=min_date.strftime('%d/%m/%Y'),
                      max_date=max_date.strftime('%d/%m/%Y'))
              )
        )
