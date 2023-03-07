from django.shortcuts import render


# Create your views here.
def manage_template(request):
    return render(request, "templates_manager/manage_template.html", {})
