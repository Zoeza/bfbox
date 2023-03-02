from django.contrib import admin
from django.db import models
from datetime import date


class Client(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    birthday = models.DateField(default=date.today())
    lawyer = models.CharField(max_length=100)

    def __str__(self):
        return self.name
