from django.shortcuts import render

# Create your views here.
def home(request):
    context = {"t_var": "t_var"}
    return render(request, "FIRSTAPPLICATION/home.html", context)
