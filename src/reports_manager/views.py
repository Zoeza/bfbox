from clients.functions import serial_number_generator
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from templates_manager.models import UploadTemplate

from .models import GeneratedReport
from . import report_actions


# --------- manage report --------#
def manage_report(request, action, sku):
    try:
        reports_list = GeneratedReport.objects.all()
    except GeneratedReport.DoesNotExist:
        raise Http404("No reports")

    url = "reports_manager/manage_report.html"

    if action == "download_report":
        return report_actions.download_report(sku)

    if action == "delete_report":
        GeneratedReport.objects.all().get(sku=sku).delete()

    if action == "print_file":
        report_actions.send_report(sku)

    context = {
        "reports_list": reports_list,
    }
    return render(request, url, context)


# --------- choose report ---------#
def choose_report(request):
    try:
        templates_list = UploadTemplate.objects.all()
    except UploadTemplate.DoesNotExist:
        raise Http404("No templates")

    url = "reports_manager/report_editor.html"

    if request.method == 'POST':
        if request.POST.get('template_name') == 'Notice letter':
            url = "reports_manager/add_report.html"
        if request.POST.get('template_name') == 'Template name':
            url = "reports_manager/test.html"

    context = {
        "templates_list": templates_list,
    }
    return render(request, url, context)


# --------- generate report -------#
def generate_report(request, action):
    if action == 'generate_notice_letter':
        report_actions.generate_notice_letter(request)
    return redirect('choose-report')
