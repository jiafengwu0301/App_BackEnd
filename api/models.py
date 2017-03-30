from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.


class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, blank=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    facebook = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.user.username
