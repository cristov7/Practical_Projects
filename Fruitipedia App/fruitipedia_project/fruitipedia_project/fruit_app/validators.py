from django.core.exceptions import ValidationError


def name_should_contain_only_letters_func(name: str) -> [ValidationError, None]:

    for char in name:

        if not char.isalpha():
            raise ValidationError('Fruit name should contain only letters!')
