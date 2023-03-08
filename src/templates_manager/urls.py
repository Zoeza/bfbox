from django.urls import path
from . import views

app_name = 'templates_manager'

urlpatterns = [

    path('manage-template/', views.manage_template, name='manage-template'),
    path('delete-template/<str:sku>', views.delete_template, name='delete-template'),

]
