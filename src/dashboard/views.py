from django.shortcuts import render, redirect
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

    if not request.session.get('language', None):
        request.session['language'] = 'en'
    direction = request.session.get('language')
    url = direction + "/dashboard/dashboard.html"

    context = {
        "reports_list": reports_list,
        "clients_list": clients_list,
        "appointments_list": appointments_list,

    }

    return render(request, url, context)


@login_required
def change_language(request, language):
    if language == 'en':
        request.session['language'] = 'en'
    if language == 'fr':
        request.session['language'] = 'fr'
    if language == 'ar':
        request.session['language'] = 'ar'
    return redirect('dashboard')
