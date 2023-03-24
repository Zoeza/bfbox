from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe


# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_bailiff = models.BooleanField(default=False)
    is_secretary = models.BooleanField(default=False)
