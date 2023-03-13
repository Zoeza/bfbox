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

    if request.method == 'POST':
        template_name = request.POST.get('template_name')
        if template_name == "Notice letter":
            return add_report(request, template_name)

    context = {
        # "reports": GeneratedReport.objects.all(),
        "templates": templates,
    }
    return render(request, "reports_manager/manage_report.html", context)


def add_report(request):
    if request.method == 'POST':
        template = UploadTemplate.objects.get(name="Notice Letter")
        template_path = template.template.path

        report = DocxTemplate(template_path)
        notice_letter = GeneratedReport()
        context = {
            'court_case_applicants': request.POST['court_case_applicants'],
            'bailiff_name': request.POST['bailiff_name'],
            'court_case_num': request.POST['court_case_num'],
            'bailiff_address': request.POST['bailiff_address'],
            'court_case_date': request.POST['court_case_date'],
            'court_case_time': request.POST['court_case_time'],
            'court_case_msg_title': request.POST['court_case_msg_title'],
            'court_case_lawyer': request.POST['court_case_lawyer'],
            'court_case_agent': request.POST['court_case_agent'],
            'court_case_defendants': request.POST['court_case_defendants'],
            'court_case_msg_content': request.POST['court_case_msg_content'],

        }

        report.render(context)
        report_io = io.BytesIO()  # create a file-like object
        report.save(report_io)  # save data to file-like object
        report_io.seek(0)  # go to the beginning of the file-like object
        # return FileResponse(report_io, as_attachment=True, filename=f'notice_letter.docx')

        notice_letter.file.save('notice_letter.docx', ContentFile(report_io.read()))
        notice_letter.filename = request.POST['court_case_num']
        notice_letter.client = request.POST['court_case_applicants']
        notice_letter.lawyer = request.POST['court_case_lawyer']
        notice_letter.save()
        messages.success(request, " New Report Generated successfully !!")
        return render(request, "reports_manager/add_report.html", {'sku': notice_letter.id})

    return redirect('reports-manager:add-report')


def download_report(request, id):
    report = GeneratedReport.objects.get(id=id)
    return FileResponse(report.file, as_attachment=True)
