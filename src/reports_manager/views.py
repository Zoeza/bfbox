from clients.functions import serial_number_generator
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from templates_manager.models import UploadTemplate

from .models import GeneratedReport
from . import report_actions


def manage_report(request, action, sku):
    try:
        templates_list = UploadTemplate.objects.all()
    except UploadTemplate.DoesNotExist:
        raise Http404("No templates")

    try:
        reports_list = GeneratedReport.objects.all()
    except GeneratedReport.DoesNotExist:
        raise Http404("No reports")

    url = "reports_manager/manage_report.html"

    if action == "download_report":
        return report_actions.download_report(sku)

    if action == "delete_report":
        GeneratedReport.objects.all().get(sku=sku).delete()

    if request.method == 'POST':
        template_name = request.POST.get('template.name')
        if template_name == 'Notice letter':
            # url = report_actions.add_notice_letter(request).get('url')
            url = "reports_manager/add_report.html"
    context = {
        "reports_list": reports_list,
        "templates_list": templates_list,
    }
    return render(request, "reports_manager/add_report.html", context)


def add_report(request):
    url = "reports_manager/add_report.html"
    if request.method == 'POST':
        template_name = request.POST.get('template.name'),
        if template_name == 'Notice letter':
            if request.method == 'POST':
                add_notice_letter(request)
                messages.success(request, " New Report Generated successfully !!")
                return redirect('manage-report')

    return render(request, url, {})


def add_notice_letter(request):
    if request.method == 'POST':
        context = {
            'court_case_applicants': request.POST.get('court_case_applicants'),
            'bailiff_name': request.POST.get('bailiff_name'),
            'court_case_num': request.POST.get('court_case_num'),
            'bailiff_address': request.POST.get('bailiff_address'),
            'court_case_date': request.POST.get('court_case_date'),
            'court_case_time': request.POST.get('court_case_time'),
            'court_case_msg_title': request.POST.get('court_case_msg_title'),
            'court_case_lawyer': request.POST.get('court_case_lawyer'),
            'court_case_agent': request.POST.get('court_case_agent'),
            'court_case_defendants': request.POST.get('court_case_defendants'),
            'court_case_msg_content': request.POST.get('court_case_msg_content'),
        }
        file = report_actions.generate_report('Notice letter', context)
        notice_letter = GeneratedReport()
        notice_letter.file.save('Notice_letter.docx', file)
        notice_letter.filename = 'Notice letter'
        notice_letter.number = request.POST.get('court_case_num')
        notice_letter.sku = serial_number_generator(10).upper()
        notice_letter.save()
