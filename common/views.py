from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "common/index.html", {})


def home(request):
    groups = ["admin", "docente", "evaluacion", "control_estudio", "coordinador"]
    return render(request, "common/home.html", {"groups": groups})
