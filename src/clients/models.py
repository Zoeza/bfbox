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
    created_date = models.DateField(default=date.today())

    def __str__(self):
        return self.name
