from django.db import models


class ProfileModel(models.Model):
    first_name = models.CharField(max_length=20)

    last_name = models.CharField(max_length=20)

    age = models.IntegerField()

    image_url = models.URLField()

    @property   # getter
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'


class NoteModel(models.Model):
    title = models.CharField(max_length=30)

    content = models.TextField()

    image_url = models.URLField()

    # Many-to-One Relationship: Many NoteModel objects - to - One ProfileModel object
    profile = models.ForeignKey(to=ProfileModel, on_delete=models.CASCADE)
