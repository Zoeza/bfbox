from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [

    path('add-client/', views.add_client, name='add-client'),
    path('manage-client/', views.manage_client, name='manage-client'),
    path('edit-client/<int:id>', views.edit_client, name='edit-client'),
    path('delete-client/<int:id>', views.delete_client, name='delete-client'),
    path('update-client/<int:id>', views.update_client, name='update-client'),


]

