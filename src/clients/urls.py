from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [

    path('manage-client/', views.manage_client, name='manage-client'),
    path('add-client/', views.add_client, name='add-client'),
    path('delete-client/<int:id>', views.delete_client, name='delete-client'),



]
