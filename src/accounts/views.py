from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import user_type, User


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        bailiff = request.POST.get('is_bailiff')
        employee = request.POST.get('is_employee')

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save()

        usertype = None
        if bailiff:
            usertype = user_type(user=user, is_bailiff=True)
        elif employee:
            usertype = user_type(user=user, is_employee=True)

        usertype.save()
        # Successfully registered. Redirect to homepage
        return redirect('sign-in')
    return render(request, "accounts/register.html", {})


def sign_in(request):
    return render(request, "accounts/sign_in.html", {})
