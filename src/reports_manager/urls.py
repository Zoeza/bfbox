from django.urls import path
from . import views

app_name = 'reports_manager'

urlpatterns = [

    path('manage-report/', views.manage_report, name='manage-report'),
    path('add-report/', views.add_report, name='add-report'),
    path('download-report/<int:id>', views.download_report, name='download-report'),

]
