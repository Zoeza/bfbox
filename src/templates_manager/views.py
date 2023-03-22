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


# ------------------------ add client -------------------------- #

def upload_template(request):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        template = request.FILES.get('template')
        last_modified = request.POST.get('last_modified', False)
        sku = serial_number_generator(10).upper()
        UploadTemplate(name=name,
                       last_modified=last_modified,
                       template=template,
                       sku=sku,
                       ).save()
    return redirect('templates_manager:manage-template')


# --------------------- delete template ------------------------ #

def delete_template(request, sku):
    UploadTemplate.objects.all().get(sku=sku).delete()
    return redirect('templates_manager:manage-template')


# ----------------------- edit template ------------------------- #

def edit_template(request, sku):
    selected_template = UploadTemplate.objects.all().get(sku=sku)
    if request.method == 'POST':
        name = request.POST.get('name', False)
        template = request.FILES.get('template')
        last_modified = request.POST.get('last_modified', False)

        if name:
            selected_template.name = name
        if template:
            selected_template.template = template
        if last_modified:
            selected_template.last_modified = last_modified

        selected_template.save()
        return redirect('templates_manager:manage-template')

    context = {
        'selected_template': selected_template
    }

    return render(request, "templates_manager/edit_template.html", context)


# ----------------------- download template ------------------------- #

def download_template(request,sku):
    template_selected = UploadTemplate.objects.get(sku=sku)
    return FileResponse(template_selected.template, as_attachment=True)
