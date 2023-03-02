from django.urls import path
from . import views


urlpatterns = [

    path('add-client/', views.add_client, name='add-client'),
    path('manage-client/', views.manage_client, name='manage-client'),



]
