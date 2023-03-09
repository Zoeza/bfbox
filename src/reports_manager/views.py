from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse

from clients.functions import serial_number_generator


def manage_report(request):

    return render(request, "templates_reports/manage_report.html", {})

