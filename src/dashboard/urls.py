from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('<str:language>/change-language/', views.change_language, name='change-language'),

]
