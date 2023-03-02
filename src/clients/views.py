from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Client


def add_client(request):
    return render(request, "clients/add_client.html", {})


def manage_client(request):
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, "clients/list_client.html", context)


def edit_client(request, id):
    obj = Client.objects.get(id=id)
    context = {
        "name": obj.name,
        "email": obj.email,
        "phone": obj.phone,
        "birthday": obj.birthday,
        "lawyer": obj.lawyer,
        "address": obj.address,
        "id": obj.id
    }
    return render(request, "clients/edit_client.html", context)


def delete_client(request, id):
    obj = Client.objects.get(id=id)
    obj.delete()
    return redirect('clients:manage-client')


def update_client(request, id):
    obj = Client(id=id)
    obj.name = request.POST['name']
    obj.email = request.POST['email']
    obj.phone = request.POST['phone']
    obj.birthday = request.POST['birthday']
    obj.lawyer = request.POST['lawyer']
    obj.address = request.POST['address']
    obj.save()
    return redirect('clients:manage-client')
