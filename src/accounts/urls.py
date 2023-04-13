from django.urls import path
from . import views

urlpatterns = [

    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('<str:action>/<email>/manage-user/', views.manage_user, name='manage-user'),
    path('<int:pk>/view-profile/', views.view_profile, name='view-profile'),
    path('update-password/', views.update_password, name='update-password'),

]