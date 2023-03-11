from django.urls import path
from . import views

app_name = 'reports_manager'

urlpatterns = [

    path('manage-report/', views.manage_report, name='manage-report'),
    path('add-report/<str:template_name>', views.add_report, name='add-report'),

]