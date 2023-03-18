from django.urls import path
from . import views

urlpatterns = [

    path('manage-report/', views.manage_report, name='manage-report'),
    path('<str:action>/add-report/', views.add_report, name='add-report'),

]
