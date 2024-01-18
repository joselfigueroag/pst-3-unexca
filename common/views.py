from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Country, State, Municipality
from .serializers import CountrySerializer, StateSerializer, MunicipalitySerializer


@login_required(login_url="login")
def home(request):
    groups = ["admin", "docente", "evaluacion", "control_estudio", "coordinador"]
    return render(request, "common/home.html", {"groups": groups})


@api_view(["GET"])
def country_detail_view(request, country_id):
    country = Country.objects.get(pk=country_id)
    serializer = CountrySerializer(country)
    return Response(serializer.data)


@api_view(["GET"])
def state_detail_view(request, state_id):
    state = State.objects.get(pk=state_id)
    serializer = StateSerializer(state)
    return Response(serializer.data)


@api_view(["GET"])
def municipality_detail_view(request, municipality_id):
    municipality = Municipality.objects.get(pk=municipality_id)
    serializer = MunicipalitySerializer(municipality)
    return Response(serializer.data)
