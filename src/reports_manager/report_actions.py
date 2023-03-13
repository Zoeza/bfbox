import io
import os

from django.http import FileResponse
from django.shortcuts import render, redirect
from templates_manager.models import UploadTemplate
from .models import GeneratedReport
from django.core.files.base import ContentFile
from django.contrib import messages
from docxtpl import DocxTemplate


def add_notice_letter(request, template_name):
    if request.method == 'POST':
        template = UploadTemplate.objects.get(name=template_name)
        template_path = template.template.path
        report = DocxTemplate(template_path)
        notice_letter = GeneratedReport()

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

        report.render(context)
        report_io = io.BytesIO()  # create a file-like object
        report.save(report_io)  # save data to file-like object
        report_io.seek(0)  # go to the beginning of the file-like object
        return FileResponse(report_io, as_attachment=True, filename=f'notice_letter.docx')

        # notice_letter.file.save('notice_letter.docx', ContentFile(report_io.read()))
        # notice_letter.filename = request.POST.get('court_case_num')
        # notice_letter.client = request.POST.get('court_case_applicants')
        # notice_letter.lawyer = request.POST.get('court_case_lawyer')
        # notice_letter.save()
        messages.success(request, " New Report Generated successfully !!")
        return FileResponse(report_io, as_attachment=True, filename=f'notice_letter.docx')

        # return render(request, "reports_manager/add_report.html", {'sku': notice_letter.id})

    return render(request, "reports_manager/add_report.html", {'template_name': template_name})
