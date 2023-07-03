from django.db import models
from django.core import validators
from .validators import *
from car_collection_project.profile_app.models import *


class CarModel(models.Model):
    CAR_TYPES = (('Sports Car', 'Sports Car'),
                 ('Pickup', 'Pickup'),
                 ('Crossover', 'Crossover'),
                 ('Minibus', 'Minibus'),
                 ('Other', 'Other'))

    car_type = models.CharField(choices=CAR_TYPES,
                                blank=False, null=False,
                                max_length=10)

    car_model = models.CharField(blank=False, null=False,
                                 max_length=20,
                                 validators=[validators.MinLengthValidator(2)])

    year = models.IntegerField(blank=False, null=False,
                               validators=[valid_year_func])

    image_url = models.URLField(blank=False, null=False)

    price = models.FloatField(blank=False, null=False,
                              validators=[validators.MinValueValidator(1)])

    # Many CarModel objects - to - One ProfileModel object -> Relationship:
    profile = models.ForeignKey(to=ProfileModel, on_delete=models.CASCADE)
