from django.db import models


class UploadTemplate(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, null=True, blank=True)
    template = models.FileField(upload_to='file_uploader/', null=True)
    sku = models.CharField(max_length=20, unique=True, null=True)
    last_modified = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
