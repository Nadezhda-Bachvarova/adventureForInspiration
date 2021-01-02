from django.core.exceptions import ValidationError


def validate_email(value):
    result = all(',' in x for x in value if x % 2 == 0)
    if result:
        raise ValidationError('The ingredients should be separated by ", "!')