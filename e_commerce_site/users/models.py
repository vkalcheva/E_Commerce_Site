from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    name = models.CharField(max_length=200,)
    email = models.EmailField(max_length=500,)

    def __str__(self):
        return self.name




