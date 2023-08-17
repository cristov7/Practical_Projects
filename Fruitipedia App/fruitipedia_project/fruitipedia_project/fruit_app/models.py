from django.db import models
from django.core import validators
from .validators import name_should_contain_only_letters_func
from fruitipedia_project.profile_app.models import ProfileModel


class FruitModel(models.Model):
    name = models.CharField(blank=False, null=False,
                            max_length=30,
                            validators=[validators.MinLengthValidator(2),
                                        name_should_contain_only_letters_func])

    image_url = models.URLField(blank=False, null=False)

    description = models.TextField(blank=False, null=False)

    nutrition = models.TextField(blank=True, null=True)

    # Many - to - One Relationship: Many FruitModel objects can have only One ProfileModel object
    profile = models.ForeignKey(to=ProfileModel, on_delete=models.CASCADE)
