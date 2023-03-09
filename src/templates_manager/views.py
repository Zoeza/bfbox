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


# ------------------ end manage template ------------------------ #


# ------------------ add client --------------------------------- #

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


# ------------------ end add client ----------------------------- #

# ------------------ delete template ---------------------------- #

def delete_template(request, sku):
    UploadTemplate.objects.all().get(sku=sku).delete()

    return redirect('templates_manager:manage-template')


# ------------------ end delete template ---------------------- #

# ------------------ Update template ---------------------------- #

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

    return render(request, "templates_manager/update_template.html", context)


# ------------------ end Update template ---------------------- #

def update_template(request, id):
    selected_template = UploadTemplate(id=id)
    if request.method == 'POST':
        selected_template.name = request.POST.get('name', False)
        selected_template.last_modified = request.POST.get('last_modified', False)
        selected_template.template = request.FILES.get('template', False)
        selected_template.sku = serial_number_generator(10).upper()
        selected_template.save()
        return redirect('templates_manager:manage-template')
