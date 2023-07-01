from django.core.exceptions import ValidationError


def name_should_contain_only_letters_func(value: str):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError("Plant name should contain only letters!")
