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
