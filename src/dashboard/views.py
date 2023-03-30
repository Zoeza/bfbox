from django.shortcuts import render
from reports_manager.models import GeneratedReport
from clients.models import Client
from appointments.models import Appointment
from accounts.models import user_type
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    reports_list = GeneratedReport.objects.all()
    clients_list = Client.objects.all()
    appointments_list = Appointment.objects.all()
    usertype = 'Employee'
    if user_type.objects.get(user=request.user).is_bailiff:
        usertype = 'Bailiff'

    context = {
        "reports_list": reports_list,
        "clients_list": clients_list,
        "appointments_list": appointments_list,
        "user_type": usertype,

    }

    return render(request, "dashboard/dashboard.html", context)
