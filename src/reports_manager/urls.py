from django.urls import path
from . import views

app_name = 'reports_manager'

urlpatterns = [

    path('manage-report/', views.manage_report, name='manage-report'),


]
