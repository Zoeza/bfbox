from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Client


def manage_client(request):
    context = {
        'clients': Client.objects.all(),
    }
    return render(request, "clients/list_client.html", context)
