from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Client

# ------------------ add client
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

# ------------------ edit client
def edit_client(request, id):




# ------------------ delete client
def delete_client(request, id):
    Client.objects.all().get(id=id).delete()

    return redirect('clients:manage-client')

# ------------------ manage client
def manage_client(request):
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, "clients/manage_client.html", context)
