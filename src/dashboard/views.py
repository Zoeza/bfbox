from django.shortcuts import render


def dashboard(request):
    return render(request, "clients/add_client.html", {})