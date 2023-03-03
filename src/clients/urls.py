from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [

    path('manage-client/', views.manage_client, name='manage-client'),



]
