from django.db import models
from django.core import validators
from games_play_project.profile_app.models import ProfileModel


class GameModel(models.Model):
    CATEGORY_CHOICES = (('Action', 'Action'),
                        ('Adventure', 'Adventure'),
                        ('Puzzle', 'Puzzle'),
                        ('Strategy', 'Strategy'),
                        ('Sports', 'Sports'),
                        ('Board/Card Game', 'Board/Card Game'),
                        ('Other', 'Other'))

    title = models.CharField(blank=False, null=False,
                             max_length=30,
                             unique=True)

    category = models.CharField(blank=False, null=False,
                                max_length=15,
                                choices=CATEGORY_CHOICES)

    rating = models.FloatField(blank=False, null=False,
                               validators=[validators.MinValueValidator(0.1),
                                           validators.MaxValueValidator(5.0)])

    max_level = models.IntegerField(blank=True, null=True,
                                    validators=[validators.MinValueValidator(1)])

    image_url = models.URLField(blank=False, null=False)

    summary = models.TextField(blank=True, null=True)

    # Many-to-One Relationship: Many GameModel objects - to - One ProfileModel object
    profile = models.ForeignKey(to=ProfileModel, on_delete=models.CASCADE)
