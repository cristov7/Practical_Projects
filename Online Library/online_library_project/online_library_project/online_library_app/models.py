from django.db import models
from online_library_project.profile_app.models import ProfileModel


class BookModel(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.URLField()
    type_book = models.CharField(max_length=30)

    # Many-to-One Relationship: Many BookModel objects - to - One ProfileModel object
    profile = models.ForeignKey(to=ProfileModel, on_delete=models.CASCADE)
