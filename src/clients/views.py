from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Client
from django.contrib.auth.decorators import login_required


@login_required
def add_client(request):
    return render(request, "clients/add_client.html", {})


@login_required
def submit_client(request):
    client = Client()
    client.name = request.POST['name']
    client.email = request.POST['email']
    client.birthday = request.POST['birthday']
    client.lawyer = request.POST['lawyer']
    client.address = request.POST['address']
    client.save()
    return redirect('clients:manage-client')


@login_required
def manage_client(request):
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, "clients/list_client.html", context)


@login_required
def edit_client(request, id):
    obj = Client.objects.get(id=id)
    context = {
        "name": obj.name,
        "email": obj.email,
        "birthday": obj.birthday,
        "lawyer": obj.lawyer,
        "address": obj.address,
        "id": obj.id
    }
    return render(request, "clients/edit_client.html", context)


@login_required
def delete_client(request, id):
    obj = Client.objects.get(id=id)
    obj.delete()
    return redirect('clients:manage-client')


@login_required
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
