from django.core.exceptions import ValidationError


def valid_year_func(value: int):
    min_year = 1980
    max_year = 2049

    if (value < min_year) or (max_year < value):
        raise ValidationError(f'Year must be between {min_year} and {max_year}')
