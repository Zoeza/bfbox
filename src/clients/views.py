from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Client


def add_client(request):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        email = request.POST.get('email', False)
        birthday = request.POST.get('birthday', False)
        address = request.POST.get('address', False)
        town = request.POST.get('town', False)
        lawyer = request.POST.get('lawyer', False)
        Client(name=name,
               email=email,
               birthday=birthday,
               address=address,
               town=town,
               lawyer=lawyer,
               ).save()
    return redirect('clients:manage-client')


def delete_client(request, id):
    obj = Client.objects.get(id=id)
    obj.delete()
    context = {
        "clients": Client.objects.all()
    }
    return redirect('clients:manage-client')


def manage_client(request):
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, "clients/list_client.html", context)
