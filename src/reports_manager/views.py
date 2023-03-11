from django.shortcuts import render, redirect
from templates_manager.models import UploadTemplate
from django.http import FileResponse, HttpResponse

from clients.functions import serial_number_generator


def manage_report(request):
    context = {
        "templates": UploadTemplate.objects.all()
    }
    return render(request, "reports_manager/manage_report.html", context)


def add_report(request, name):
    return render(request, "reports_manager/add_report.html", {})
