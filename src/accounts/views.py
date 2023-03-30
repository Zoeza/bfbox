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
        usertype = request.POST.get('user-type')
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save()

        if usertype == 'Bailiff':
            usertype = user_type(user=user, is_bailiff=True)
        elif usertype == 'Employee':
            usertype = user_type(user=user, is_employee=True)

        usertype.save()
        # Successfully registered. Redirect to homepage
        return redirect('sign-in')
    return render(request, "accounts/register.html", {})


def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email value from form
        password = request.POST.get('password')  # Get password value from form
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            type_obj = user_type.objects.get(user=user)
            if user.is_authenticated and type_obj.is_bailiff:
                return redirect('dashboard')  # Go to dashboard
            elif user.is_authenticated and type_obj.is_employee:
                return redirect('dashboard')  # Go to dashboard

    return render(request, "accounts/sign_in.html", {})
