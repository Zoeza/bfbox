import io
import os
from clients.functions import serial_number_generator
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render
from templates_manager.models import UploadTemplate
from .models import GeneratedReport
from django.core.files.base import ContentFile
from docxtpl import DocxTemplate
from docx2pdf import convert
from django.core.files import File

from djangoconvertvdoctopdf.convertor import ConvertFileModelField, StreamingConvertedPdf


# import mammoth


# ------------ generate notice letter --------------#

def generate_notice_letter(request):
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
        notice_letter = GeneratedReport()
        notice_letter.file.save('Notice_letter.docx', file)
        notice_letter.filename = 'Notice letter'
        notice_letter.number = request.POST.get('court_case_num')
        notice_letter.sku = serial_number_generator(10).upper()
        notice_letter.save()


# ------------ generate report --------------#

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


# ------------ save report --------------#

def save_report(filename, court_case_num, file):
    sku = serial_number_generator(10).upper()
    GeneratedReport(filename=filename,
                    number=court_case_num,
                    file=file,
                    sku=sku,
                    ).save()


# ------------ download report --------------#

def download_report(sku):
    report_selected = GeneratedReport.objects.get(sku=sku)
    return FileResponse(report_selected.file, as_attachment=True)


# --------------- convert docx to pdf file -----------------#

def docx_to_pdf(sku):
    report_selected = GeneratedReport.objects.get(sku=sku)
    file = DocxTemplate(report_selected.file.path)
    inst = ConvertFileModelField(file)
    file = inst.get_content()
    report_selected.pdf = File(open(file.get('path'), 'rb'))
    report_selected.pdf.name = file.get('name')

    return inst.stream_content()

    # convert(report_selected.file.pa

    # report_selected.pdf.save('Notice_letter.pdf', convert(report_selected.file))
    # pdf = (report_selected.pdf.read(), 'r')
    # response = HttpResponse(pdf.read(), content_type='application/pdf')
    # response = HttpResponse(template_output)
    # response['Content-Disposition'] = 'attachment;filename=name.docx'
    # return response

    # pdf.closed
