from django.urls import path
from . import views

app_name = 'templates_manager'

urlpatterns = [

    path('manage-template/', views.manage_template, name='manage-template'),
    path('upload-template/', views.upload_template, name='upload-template'),
    path('delete-template/<str:sku>', views.delete_template, name='delete-template'),
    path('edit-template/<str:sku>', views.edit_template, name='edit-template'),
    path('download-template/<str:sku>', views.download_template, name='edit-template'),

]
