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


def generate_report(template_name, context):
    template = UploadTemplate.objects.get(name=template_name)
    template_path = template.template.path
    report = DocxTemplate(template_path)
    report.render(context)
    report_io = io.BytesIO()  # create a file-like object
    report.save(report_io)  # save data to file-like object
    report_io.seek(0)  # go to the beginning of the file-like object
    report = ContentFile(report_io.read())
    return report
