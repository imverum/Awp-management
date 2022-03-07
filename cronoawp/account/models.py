from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)

    def __str__(self):
        return f'Profile for user{self.user.username}'


