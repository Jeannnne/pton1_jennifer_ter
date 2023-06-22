from datetime import date
from django.core.exceptions import ValidationError


def validate_date_range(value):
    # Year, month, day
    min_date = date(1970, 1, 1)
    max_date = date(2050, 12, 31)

    if value < min_date or value > max_date:
        raise ValidationError(
            "La date doit être comprise entre {min_date} et {max_date}."
            .format(min_date=min_date.strftime('%d/%m/%Y'),
                    max_date=max_date.strftime('%d/%m/%Y'))
        )
