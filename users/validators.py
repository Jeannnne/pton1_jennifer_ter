import pytz
from datetime import datetime,date
from django.core.exceptions import ValidationError


def validate_date_range(value):
    # Year, month, day
    min_date = datetime(1970, 1, 1, tzinfo=pytz.UTC).date()
    max_date = datetime(2050, 12, 31, tzinfo=pytz.UTC).date()

    if isinstance(value, date):
        if value < min_date or value > max_date:
            raise ValidationError(
                "La date doit être comprise entre {min_date} et {max_date}."
                .format(min_date=min_date.strftime('%d/%m/%Y'),
                        max_date=max_date.strftime('%d/%m/%Y'))
            )
    else:
        raise ValidationError("La valeur fournie n'est pas une date valide.")