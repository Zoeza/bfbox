from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Client


def add_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        birthday = request.POST.get('birthday')
        address = request.POST.get('address')
        town = request.POST.get('town')
        lawyer = request.POST.get('lawyer')
        Client(name=name,
               email=email,
               birthday=birthday,
               address=address,
               town=town,
               lawyer=lawyer,
               ).save()
    return redirect('clients:manage-client')


def manage_client(request):
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, "clients/list_client.html", context)
