import io
import os
from django.shortcuts import render, redirect
from templates_manager.models import UploadTemplate
from .models import GeneratedReport
from . import report_actions

from django.http import FileResponse, HttpResponse

from clients.functions import serial_number_generator
from templates_manager.models import UploadTemplate
from .models import GeneratedReport
from django.core.files.base import ContentFile
from django.contrib import messages
from docxtpl import DocxTemplate


def manage_report(request):
    templates = UploadTemplate.objects.all()
    url = "reports_manager/manage_report.html"
    # if request.method == 'POST':
    #   template_name = request.POST.get('template_name')
    #  if template_name == 'Notice letter':
    #     url = "reports_manager/add_report.html"

    context = {
        "reports_list": GeneratedReport.objects.all(),
        "templates_list": templates,
    }
    return render(request, url, context)


def add_report(request, template_name):
    if request.method == 'POST':
        template_name = request.POST.get('template_name')
        if template_name == 'Notice letter':
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
                file = generate_report(template_name, context)
                notice_letter = GeneratedReport()
                notice_letter.file.save(template_name.docx, file)
                notice_letter.filename = 'Notice letter'
                notice_letter.number = request.POST.get('court_case_num')
                notice_letter.sku = serial_number_generator(10).upper()
                notice_letter.save()
                messages.success(request, " New Report Generated successfully !!")
                return redirect('reports_manager:manage-report')

    return render(request, "reports_manager/add_report.html", {})


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
