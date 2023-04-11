from clients.functions import serial_number_generator
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from templates_manager.models import UploadTemplate

from .models import GeneratedReport
from . import report_actions


# --------- manage report --------#
def manage_report(request, action, sku):
    direction = request.session.get('language')
    try:
        reports_list = GeneratedReport.objects.all()
    except GeneratedReport.DoesNotExist:
        raise Http404("No reports")

    url = direction + "/reports_manager/test.html"

    if action == "download_report":
        return report_actions.download_report(sku)

    if action == "view_report":
        return report_actions.docx_to_pdf(sku)

    if action == "delete_report":
        GeneratedReport.objects.all().get(sku=sku).delete()

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

    direction = request.session.get('language')

    url = direction + "/reports_manager/report_editor.html"

    if request.method == 'POST':
        if request.POST.get('template_name') == 'Notice letter':
            url = direction + "/reports_manager/add_report.html"
        if request.POST.get('template_name') == 'Template name':
            url = direction + "/reports_manager/test.html"

    context = {
        "templates_list": templates_list,
    }
    return render(request, url, context)


# --------- generate report -------#
def generate_report(request, action):
    if action == 'generate_notice_letter':
        report_actions.generate_notice_letter(request)
    return redirect('choose-report')
