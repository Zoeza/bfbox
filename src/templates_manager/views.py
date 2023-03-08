from django.shortcuts import render

from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from docxtpl import DocxTemplate
# Create your views here.
def manage_template(request):
    return render(request, "templates_manager/manage_template.html", {})
