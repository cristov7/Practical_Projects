from django.db import models
from django.core import validators
from .validators import *


class ProfileModel(models.Model):
    username = models.CharField(blank=False, null=False,
                                max_length=10,
                                validators=[validators.MinLengthValidator(2)])

    first_name = models.CharField(blank=False, null=False,
                                  max_length=20,
                                  validators=[name_must_start_with_a_capital_letter_func])

    last_name = models.CharField(blank=False, null=False,
                                 max_length=20,
                                 validators=[name_must_start_with_a_capital_letter_func])

    profile_picture = models.URLField(blank=True, null=True)

    @property   # getter
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
