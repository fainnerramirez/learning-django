from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "polls/index.html")

def saludo(request, name):
    return render(request, "polls/saludo.html", {
        "name": name.capitalize()
    })