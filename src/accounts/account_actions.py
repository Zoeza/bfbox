from .models import user_type, User


def add_user(request):
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
