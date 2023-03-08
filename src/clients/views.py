from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Client
from .functions import serial_number_generator


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


# ------------------ end add client ---------------------- #


# ------------------ update client ---------------------- #

def edit_client(request, sku):
    selected_client = Client.objects.get(sku=sku)
    context = {
        "name": selected_client.name,
        "email": selected_client.email,
        "birthday": selected_client.birthday,
        "lawyer": selected_client.lawyer,
        "address": selected_client.address,
        "town": selected_client.town,
        "sku": selected_client.sku
    }
    return render(request, "clients/update_client.html", context)


def update_client(request, sku):
    selected_client = Client(sku=sku)
    if request.method == 'POST':
        selected_client.name = request.POST.get('name', False)
        selected_client.email = request.POST.get('email', False)
        selected_client.birthday = request.POST.get('birthday', False)
        selected_client.lawyer = request.POST.get('lawyer', False)
        selected_client.address = request.POST.get('address', False)
        selected_client.town = request.POST.get('town', False)
        selected_client.save()
        return redirect('clients:manage-client')


# ------------------ end update client ---------------------- #


# ------------------ delete client -------------------------- #

def delete_client(request, sku):
    Client.objects.all().get(sku=sku).delete()

    return redirect('clients:manage-client')


# ------------------ end delete client ---------------------- #


# ------------------ manage client -------------------------- #

def manage_client(request):
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, "clients/manage_client.html", context)

# ------------------ end manage client ---------------------- #
