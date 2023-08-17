from django.core.exceptions import ValidationError


def consist_only_of_letters_func(value: str) -> [ValidationError, None]:

    for char in value:

        if not char.isalpha():
            raise ValidationError('The name should contain only letters!')


def contain_at_least_one_digit_func(value: str) -> [ValidationError, None]:
    digit = False

    for char in value:

        if char.isdigit():
            digit = True

            break

    if not digit:
        raise ValidationError('The password must contain at least 1 digit!')
