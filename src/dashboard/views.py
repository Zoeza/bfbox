from django.shortcuts import render
from reports_manager.models import GeneratedReport
from clients.models import Client
from appointments.models import Appointment
from accounts.models import user_type


def dashboard(request):
    reports_list = GeneratedReport.objects.all()
    clients_list = Client.objects.all()
    appointments_list = Appointment.objects.all()
    context = {
        "reports_list": reports_list,
        "clients_list": clients_list,
        "appointments_list": appointments_list,
        "user_type": user_type,

    }

    return render(request, "dashboard/dashboard.html", context)
