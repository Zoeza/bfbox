from django.urls import path
from . import views

urlpatterns = [

    path('<str:action>/<str:sku>/manage-report/', views.manage_report, name="manage-report"),
    path('<str:action>/generate-report/', views.generate_report, name="generate-report"),
    path('choose-report/', views.choose_report, name="choose-report"),

]
