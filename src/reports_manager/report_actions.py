import io
import os
from clients.functions import serial_number_generator
from django.http import FileResponse
from django.shortcuts import redirect
from templates_manager.models import UploadTemplate
from .models import GeneratedReport
from django.core.files.base import ContentFile
from docxtpl import DocxTemplate


def add_notice_letter(request):
    if request.POST.get('template.name') == 'Notice letter':
        url = "reports_manager/add_report.html"
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
            file = generate_report('Notice letter', context)
            save_report('Notice letter', request.POST.get('court_case_num'), file)
        # return redirect('manage-report')

    return {'url': url, }


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


def save_report(filename, court_case_num, file):
    sku = serial_number_generator(10).upper()
    GeneratedReport(filename=filename,
                    number=court_case_num,
                    file=file,
                    sku=sku,
                    ).save()


def download_report(sku):
    report = GeneratedReport.objects.get(sku=sku)
    return FileResponse(report.file, as_attachment=True)
