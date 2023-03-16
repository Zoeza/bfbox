from django.urls import path
from . import views

app_name = 'reports_manager'

urlpatterns = [

    path('manage-report/', views.manage_report, name='manage-report'),
    path('submit-notice-letter/', views.submit_notice_letter, name='submit-notice-letter'),
    path('download-report/<str:sku>', views.download_report, name='download-report'),

]
