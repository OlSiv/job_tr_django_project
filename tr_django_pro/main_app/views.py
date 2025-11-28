from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world!")

def page2_view(request):
    return render(request, "page2.html")
