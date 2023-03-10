from django.db import models


class GeneratedReport(models.Model):
    objects = models.Manager()
    filename = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    lawyer = models.CharField(max_length=255)
    file = models.FileField(upload_to='', null=True)
    last_modified = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.filename
