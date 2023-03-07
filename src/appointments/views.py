from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Appointment
import random
import string


# ------------------ add appointment ---------------------- #

def add_appointment(request):
    if request.method == 'POST':
        title = request.POST.get('title', False)
        client_name = request.POST.get('email', False)
        time = request.POST.get('address', False)
        sku = serial_number_generator(10).upper()

        Appointment(title=title,
                    client_name=client_name,
                    time=time,
                    sku=sku,
                    ).save()
    return redirect('appointments:manage-appointment')


# ------------------ update appointment ---------------------- #

def edit_appointment(request, id):
    selected_appointment = Appointment.objects.get(id=id)
    context = {
        "title": selected_appointment.title,
        "client_name": selected_appointment.client_name,
        "time": selected_appointment.time,
        "id": selected_appointment.id
    }
    return render(request, "appointments/update_appointment.html", context)


def update_appointment(request, id):
    selected_appointment = Appointment(id=id)
    if request.method == 'POST':
        selected_appointment.title = request.POST.get('title', False)
        selected_appointment.client_name = request.POST.get('client_name', False)
        selected_appointment.time = request.POST.get('time', False)
        selected_appointment.sku = serial_number_generator(10).upper()
        selected_appointment.save()
        return redirect('appointments:manage-appointment')


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


def serial_number_generator(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str
