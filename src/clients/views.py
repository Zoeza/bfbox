from django.shortcuts import render, redirect
from .models import Client


# Create your views here.
def add_client(request):
    if request.method == 'POST':
        client = Client()
        client.name = request.POST['name']
        client.email = request.POST['email']
        client.phone = request.POST['phone']
        client.birthday = request.POST['birthday']
        client.lawyer = request.POST['lawyer']
        client.address = request.POST['address']
        client.save()
        return redirect('clients:manage-client')

    return render(request, "clients/add_client.html", {})


def manage_client(request):
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, "clients/list_client.html", context)
