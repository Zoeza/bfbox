from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
from .models import UploadTemplate
from clients.functions import serial_number_generator


# ------------------ manage template -------------------------- #

def manage_template(request):
    context = {
        "templates": UploadTemplate.objects.all()
    }
    return render(request, "templates_manager/manage_template.html", context)


# ------------------ end manage template ---------------------- #

# ------------------ add client ---------------------- #

def upload_template(request):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        template = request.FILES.get('template', False)
        modified_at = request.POST.get('birthday', False)
        sku = serial_number_generator(10).upper()
        UploadTemplate(name=name,
                       modified_at=modified_at,
                       template=template,
                       sku=sku,
                       ).save()
    return redirect('templates_manager:manage-template')


# ------------------ end add client ---------------------- #
# ------------------ delete template -------------------------- #

def delete_template(request, sku):
    UploadTemplate.objects.all().get(sku=sku).delete()

    return redirect('templates_manager:manage-template')

# ------------------ end delete template ---------------------- #
