from django.contrib import admin
from django.db import models
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    address = models.CharField(max_length=100)
    birthday = models.DateField(default=date.today())
    lawyer = models.CharField(max_length=100)

    def __str__(self):
        return self.name
