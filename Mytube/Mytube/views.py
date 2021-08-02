from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hi this is home")
    return render(request, "home.html")
