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


# ------------------ edit client ---------------------- #

def edit_client(request, sku):
    selected_client = Client.objects.all().get(sku=sku)
    direction = request.session.get('language')
    url = direction + "/clients/edit_client.html"
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

    context = {
        'selected_client': selected_client
    }

    return render(request, url, context)


# ------------------ end edit client ---------------------- #


# ------------------ delete client -------------------------- #

def delete_client(request, sku):
    Client.objects.all().get(sku=sku).delete()

    return redirect('clients:manage-client')


# ------------------ end delete client ---------------------- #


# ------------------ manage client -------------------------- #

def manage_client(request):
    direction = request.session.get('language')
    url = direction + "/clients/manage_client.html"

    context = {
        'clients': Client.objects.all(),
    }
    return render(request, url, context)

# ------------------ end manage client ---------------------- #
