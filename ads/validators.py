import dateutil.utils
from dateutil.relativedelta import relativedelta
from datetime import date
from rest_framework.exceptions import ValidationError

FORBIDDEN_DOMEN = ["rambler.ru"]
MIN_AGE = 9


def check_birth_date(value):
    diff = relativedelta(date.today(), value).years
    if diff < MIN_AGE:
        raise ValidationError(f"User with age {diff} is too young!")


def check_email(value):
    mail_domen = value.split("@")[-1]
    if mail_domen in FORBIDDEN_DOMEN:
        raise ValidationError(f"{mail_domen} is forbidden!")
