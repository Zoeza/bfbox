from django.shortcuts import render, redirect
from templates_manager.models import UploadTemplate
from .models import GeneratedReport
from . import report_actions

from django.http import FileResponse, HttpResponse

from clients.functions import serial_number_generator


def manage_report(request):
    templates = UploadTemplate.objects.all()

    if request.method == 'POST':
        template_name = request.POST.get('template_name')
        if template_name == "Notice letter":
            return report_actions.add_notice_letter(request, template_name)

    context = {
        # "reports": GeneratedReport.objects.all(),
        "templates": templates,
    }
    return render(request,"reports_manager/manage_report.html", context)


def add_report(request):
    if request.method == 'POST':
        template_name = request.POST.get('template_name')
        if template_name == "Notice letter":
            url = report_actions.add_notice_letter(request).get('url')

        return render(request, url, {'template_name': template_name})
