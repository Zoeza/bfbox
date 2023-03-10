from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [

    path('manage-client/', views.manage_client, name='manage-client'),
    path('add-client/', views.add_client, name='add-client'),
    path('delete-client/<str:sku>', views.delete_client, name='delete-client'),
    path('edit-client/<str:sku>', views.edit_client, name='edit-client'),

]
