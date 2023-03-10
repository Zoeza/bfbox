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
    sku = models.CharField(max_length=20, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
