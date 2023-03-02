from django.shortcuts import render


def dashboard(request):
    return render(request, "clients/list_client.html", {})