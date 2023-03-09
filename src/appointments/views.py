from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Appointment
from clients.functions import serial_number_generator


# ------------------ add appointment ---------------------- #

def add_appointment(request):
    if request.method == 'POST':
        title = request.POST.get('title', False)
        client_name = request.POST.get('email', False)
        time = request.POST.get('time', False)
        sku = serial_number_generator(10).upper()

        Appointment(title=title,
                    client_name=client_name,
                    time=time,
                    sku=sku,
                    ).save()
    return redirect('appointments:manage-appointment')


# ------------------ update appointment ---------------------- #

def edit_appointment(request, sku):
    selected_appointment = Appointment.objects.get(sku=sku)
    if request.method == 'POST':
        title = request.POST.get('title', False)
        client_name = request.POST.get('client_name', False)
        time = request.POST.get('time', False)

        if title:
            selected_appointment.title = title
        if client_name:
            selected_appointment.client_name = client_name
        if time:
            selected_appointment.time = time

        selected_appointment.save()
        return redirect('appointments:manage-appointment')

    context = {
        'selected_appointment': selected_appointment
    }

    return render(request, "appointments/edit_appointment.html", context)


# ------------------ delete appointment --------------------- #

def delete_appointment(request, sku):
    Appointment.objects.all().get(sku=sku).delete()

    return redirect('appointments:manage-appointment')


# ------------------ manage client -------------------- #

def manage_appointment(request):
    context = {
        'appointments': Appointment.objects.all(),
    }
    return render(request, "appointments/manage_appointment.html", context)



