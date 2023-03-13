from django.shortcuts import render, redirect
from templates_manager.models import UploadTemplate
from docxtpl import DocxTemplate


def add_notice_letter(request, template_name):
    url = "reports_manager/add_report.html"
    return {'url': url, }
