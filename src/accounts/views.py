from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import user_type, User
from django.contrib.auth.decorators import login_required
from . import account_actions


# Create your views here.
# ------------ sign up page -------------#
def sign_up(request):
    if not request.session.get('language', None):
        request.session['language'] = 'ar'
    direction = request.session.get('language')

    url = direction + "/accounts/register.html"
    account_actions.add_user(request)
    return render(request, url, {})


# ------------ sign in page -------------#
def sign_in(request):
    if not request.session.get('language', None):
        request.session['language'] = 'ar'
    direction = request.session.get('language')
    url = direction + "/accounts/sign_in.html"

    if request.method == 'POST':
        user = authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Go to dashboard

        else:
            return render(request, url, {'error': 'Username or password is incorrect!'})
    else:
        return render(request, url, {})


# ------------ sign out page -------------#
@login_required
def sign_out(request):
    logout(request)
    return redirect('sign-in')


# ------------ user management -------------#
@login_required
def manage_user(request, action, email):
    direction = request.session.get('language')
    try:
        users_list = User.objects.all()
        usertype_list = user_type.objects.all()
    except User.DoesNotExist:
        raise Http404("No users")

    url = direction + "/accounts/manage_user.html"
    if action == "add_user":
        account_actions.add_user(request)
    if action == "delete_user":
        user = User.objects.all().get(email=email)
        user.is_active = False
        user.save()

    context = {
        "users_list": users_list,
        "usertype_list": usertype_list,

    }
    return render(request, url, context)
