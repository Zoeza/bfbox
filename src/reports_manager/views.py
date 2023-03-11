from django.shortcuts import render, redirect
from template_manager.models import UploadTemplate
from django.http import FileResponse, HttpResponse

from clients.functions import serial_number_generator


def manage_report(request):
    templates = UploadTemplate.objects.all()
    context = {
        "templates": templates
    }
    return render(request, "reports_manager/manage_report.html", context)


def add_report(request):
    return render(request, "reports_manager/add_report.html", {})
