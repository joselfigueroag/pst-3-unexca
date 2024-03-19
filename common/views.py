from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Country, State, Municipality
from .serializers import CountrySerializer, StateSerializer, MunicipalitySerializer
from academic_data.models import AcademicPeriod
from students.models import StudentDetail


def check_user_type(function):
    def wrap(request, *args, **kwargs):
        try:
            user_group = request.user.group.name
        except:
            user_group = request.request.user.group.name
        kwargs["user_group"] = user_group
        return function(request, *args, **kwargs)
    return wrap


@check_user_type
@login_required(login_url="login")
def home(request, **kwargs):
    is_home = request.path == '/home/'
    groups = ["admin", "docente", "evaluacion", "control_estudio", "coordinador"]
    user_group = kwargs.get("user_group")
    return render(request, "common/home.jinja", {"groups": groups, "user_group": user_group, 'is_home': is_home})


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


@login_required(login_url="login")
def stats(request):
    return render(request, "common/stats.html")


@check_user_type
@login_required
def pie_chart_varones_hembras(request, **kwargs):
    today = datetime.now()

    if today.month < 7:
        period = AcademicPeriod.objects.filter(period__endswith=today.year).first()
    else:
        period = AcademicPeriod.objects.filter(period__startswith=today.year).first()
    
    varones = 0
    hembras = 0
    if period:
        students = StudentDetail.objects.filter(periodo_id=period.id)
        varones += students.filter(genero="masculino").count()
        hembras += students.filter(genero="femenino").count()

    data = {
        'labels': ['Hembras', 'Varones'],
        'datasets': [{
            'data': [hembras, varones],
            'backgroundColor': ['rgba(255, 99, 132, 0.5)', 'rgba(54, 162, 235, 0.5)']
        }]
    }

    data.update(kwargs)
    return JsonResponse(data)


@check_user_type
@login_required
def bar_char_cuadro_honor(request, **kwargs):
    """datos = {}
    data_chart = {}
    cantidad_materias = {}
    matriculas_s = {}
    period = AcademicPeriod.objects.order_by('-id').first()
    matriculas = Tuition.objects.filter(academic_period_id=period.id)
    for matricula in matriculas:
      promedio_por_alumno = AllNotes.objects.filter(periodo=period,matricula=matricula.id)
      for item in promedio_por_alumno:
        student_id = item.student_id
        full_name = item.p_nombre +" "+ item.p_apellido +" "+ item.cedula
        if item.student_id not in datos:
          datos[item.student_id] = float(item.definitiva)
          cantidad_materias[item.student_id] = 1
        else:
          datos[item.student_id] += float(item.definitiva)
          cantidad_materias[item.student_id] += 1
        matriculas_s[item.student_id] = matricula
        
      for student_id, total_definitiva in datos.items():
          cantidad_materias_estudiante = cantidad_materias.get(student_id, 1)  # En caso de que no haya materias para el estudiante
          print(f"Estudiante ID: {full_name}, Total Definitiva: {total_definitiva}, Cantidad de Materias: {cantidad_materias_estudiante}")
          promedio = total_definitiva / cantidad_materias_estudiante
          datos[student_id] = promedio

    data_chart = {
    'labels': [],  # Etiquetas para cada estudiante
    'datasets': [{
        'label': [],  # Etiqueta del conjunto de datos
        'data': [],  # Datos de los promedios de notas para cada estudiante
        'backgroundColor': 'rgba(54, 162, 235, 0.5)'  # Color de fondo de las barras
    }]
    }
    for student_id, promedio in datos.items():
      data_chart['datasets'][0]['label'].append(str(matriculas_s[student_id]))
      print(matriculas_s[student_id])
      # Agregar el ID del estudiante como etiqueta
      data_chart['labels'].append(full_name)
      # Agregar el promedio de notas para el estudiante
      data_chart['datasets'][0]['data'].append(promedio)"""
  
    return JsonResponse({"uno":"1"})
