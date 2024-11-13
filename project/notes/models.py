from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Note(models.Model):
    note = models.CharField(max_length=255)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.note