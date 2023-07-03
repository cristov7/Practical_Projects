from django.core.exceptions import ValidationError


def consist_of_minimum_characters_func(value: str):
    min_chars = 2

    if len(value) < min_chars:
        raise ValidationError(f'The username must be a minimum of {min_chars} chars')
