from django.core.exceptions import ValidationError


def name_must_start_with_a_capital_letter_func(value: str):
    first_letter = value[0]

    if first_letter.islower():
        raise ValidationError("Your name must start with a capital letter!")
