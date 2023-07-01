from django.db import models
from django.core import validators
from .validators import *
from my_plant_project.profile_app.models import *


class PlantModel(models.Model):
    PLANT_TYPE_CHOICE = (("Outdoor Plants", "Outdoor Plants"),
                         ("Indoor Plants", "Indoor Plants"))

    plant_type = models.CharField(blank=False, null=False,
                                  max_length=14,
                                  choices=PLANT_TYPE_CHOICE)

    name = models.CharField(blank=False, null=False,
                            max_length=20,
                            validators=[validators.MinLengthValidator(2),
                                        name_should_contain_only_letters_func])

    image_url = models.URLField(blank=False, null=False)

    description = models.TextField(blank=False, null=False)

    price = models.FloatField(blank=False, null=False)

    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
