from django.db import models
from datetime import date


class Client(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birthday = models.DateField(default=date.today())
    address = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    lawyer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
