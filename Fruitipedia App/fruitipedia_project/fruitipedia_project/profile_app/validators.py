from django.core.exceptions import ValidationError


def name_must_start_with_a_letter_func(name: str) -> [ValidationError, None]:

    char = name[0]

    if not char.isalpha():
        raise ValidationError('Your name must start with a letter!')
