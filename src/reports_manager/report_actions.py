from django.shortcuts import render, redirect
from templates_manager.models import UploadTemplate


def add_notice_letter(request):
    url = "reports_manager/add_report.html"
    return {'url': url, }
