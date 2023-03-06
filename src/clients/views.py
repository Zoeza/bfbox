from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Client
import random
import string


# ------------------ add client ---------------------- #

def add_client(request):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        email = request.POST.get('email', False)
        birthday = request.POST.get('birthday', False)
        address = request.POST.get('address', False)
        town = request.POST.get('town', False)
        lawyer = request.POST.get('lawyer', False)
        sku = serial_number_generator(10).upper()

        Client(name=name,
               email=email,
               birthday=birthday,
               address=address,
               town=town,
               sku=sku,
               lawyer=lawyer,
               ).save()
    return redirect('clients:manage-client')


# ------------------ update client ---------------------- #

def update_client(request,id):
    selected_client = Client.objects.all().get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name', False)
        email = request.POST.get('email', False)
        birthday = request.POST.get('birthday', False)
        address = request.POST.get('address', False)
        town = request.POST.get('town', False)
        lawyer = request.POST.get('lawyer', False)

        if name:
            selected_client.name = name
        if email:
            selected_client.email = email
        if birthday:
            selected_client.birthday = birthday
        if address:
            selected_client.address = address
        if town:
            selected_client.town = town
        if lawyer:
            selected_client.lawyer = lawyer
        selected_client.save()
        return redirect('clients:manage-client')
    else:
        return redirect('clients:update-client')


# ------------------ delete client --------------------- #

def delete_client(request, sku):
    Client.objects.all().get(sku=sku).delete()

    return redirect('clients:manage-client')


# ------------------ manage client -------------------- #

def manage_client(request):
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, "clients/manage_client.html", context)


def serial_number_generator(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str
