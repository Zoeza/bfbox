import io
import os

from django.http import FileResponse
from templates_manager.models import UploadTemplate
from .models import GeneratedReport
from django.core.files.base import ContentFile
from docxtpl import DocxTemplate


def download_report(request, sku):
    report = GeneratedReport.objects.get(sku=sku)
    return FileResponse(report.file, as_attachment=True)


