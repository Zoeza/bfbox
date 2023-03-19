from django.urls import path
from . import views

urlpatterns = [

    path('<str:action>/<str:sku>/manage-report/', views.manage_report, name='manage-report'),
    path('<str:action>/<str:template_name>/add-report/', views.add_report, name='add-report'),

]
