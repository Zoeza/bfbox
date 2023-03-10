from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('manage-appointment/', views.manage_appointment, name='manage-appointment'),
    path('add-appointment/', views.add_appointment, name='add-appointment'),
    path('delete-appointment/<str:sku>', views.delete_appointment, name='delete-appointment'),
    path('edit-appointment/<str:sku>', views.edit_appointment, name='edit-appointment'),

]
