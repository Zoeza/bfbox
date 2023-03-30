from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import user_type, User
from django.contrib.auth.decorators import login_required


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
        user = authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Go to dashboard

        else:
            return render(request, "accounts/sign_in.html", {'error': 'Username or password is incorrect!'})
    else:
        return render(request, "accounts/sign_in.html", {})


@login_required
def sign_out(request):
    logout(request)
    return redirect('sign-in')
