from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="login")
def home(request):
    groups = ["admin", "docente", "evaluacion", "control_estudio", "coordinador"]
    return render(request, "common/home.html", {"groups": groups})
