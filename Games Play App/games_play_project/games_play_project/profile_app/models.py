from django.db import models
from django.core import validators


class ProfileModel(models.Model):
    email = models.EmailField(blank=False, null=False)

    age = models.IntegerField(blank=False, null=False,
                              validators=[validators.MinValueValidator(12)])

    password = models.CharField(blank=False, null=False,
                                max_length=30)

    first_name = models.CharField(blank=True, null=True,
                                  max_length=30)

    last_name = models.CharField(blank=True, null=True,
                                 max_length=30)

    profile_picture = models.URLField(blank=True, null=True)

    @property   # getter
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
