from django.db import models


class ProfileModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image_url = models.URLField()

    @property   # getter
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
