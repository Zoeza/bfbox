from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from .models import UploadTemplate


# ------------------ manage template -------------------------- #

def manage_template(request):
    context = {
        "templates": UploadTemplate.objects.all()
    }
    return render(request, "templates_manager/manage_template.html", context)
# ------------------ end manage template ---------------------- #


# ------------------ delete template -------------------------- #

def delete_template(request, sku):
    UploadTemplate.objects.all().get(sku=sku).delete()

    return redirect('templates_manager:manage-template')


# ------------------ end delete template ---------------------- #


