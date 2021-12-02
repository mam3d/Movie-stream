import re
from django.core.exceptions import ValidationError


def phone_validator(value):
    pattern = r"09\d{9}$"

    if not re.match(pattern,value):
        raise ValidationError("please enter correct format ex 0912***2029")
    return value