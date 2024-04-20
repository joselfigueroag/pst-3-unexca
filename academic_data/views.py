from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.db.models import Prefetch
from decimal import Decimal

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from common.models import Country, Moment
from common.views import check_user_type
from students.models import Student
from .models import Section, Grade, Subject, Teacher, AcademicPeriod, Tuition, Qualification, AllNotes
from .forms import SectionForm, GradeForm, SubjectForm, TeacherForm, AcademicPeriodForm, TuitionForm
from .serializers import TuitionSerializer

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
from datetime import datetime
from django.urls import reverse_lazy


#SECCIONES
@method_decorator(login_required, name="dispatch")
class SectionView(View):
  def __init__(self, *args, **kwargs):
    self.form = SectionForm
    self.sections = Section.objects.all()
  
  @check_user_type
  def get(self, request, *args, **kwargs):
    user_group = kwargs.get("user_group")
    if "section_id" in kwargs:
      self.sections.get(pk=kwargs["section_id"]).delete()
      messages.info(request, message="Seccion eliminada")
      return redirect('sections')
    else:
      return render(
        request,
        "academic_data/sections/sections.html",
        {"sections": self.sections, "form": self.form, "user_group": user_group}
      )

  def post(self, request, **kwargs):
    section_form = self.form(request.POST)
    if section_form.is_valid():
      try:
        section_form.save()
        messages.success(request, message="Seccion creada con exito")
      except:
        messages.error(request, message="Error la base de datos")
    else:
      errors = [error for error in section_form.errors.values()]
      messages.error(request, message=f"{errors[0][0]}")
    return redirect('sections')
  
  def put(self, request, section_id):
    instance = self.sections.get(pk=section_id)
    section_form = self.form(request.PUT, instance=instance)
    if section_form.is_valid():
      try:
        section_form.save()
        messages.success(request, message="Seccion actualizada con exito")
      except:
        messages.error(request, message="Error la base de datos")
    else:
      errors = [error for error in section_form.errors.values()]
      messages.error(request, message=f"{errors[0][0]}")
    return redirect('sections')


#GRADOS
@method_decorator(login_required, name="dispatch")
class GradeView(View):
  def __init__(self, *args, **kwargs):
    self.form = GradeForm
    self.grades = Grade.objects.all()

  @check_user_type
  def get(self, request, *args, **kwargs):
    user_group = kwargs.get("user_group")
    if "grade_id" in kwargs:
      self.grades.get(pk=kwargs["grade_id"]).delete()
      messages.info(request, message="Grado eliminado")
      return redirect('grades')
    else:
      return render(
        request,
        "academic_data/grades/grades.jinja",
        {"grades": self.grades, "form": self.form, "user_group": user_group}
      )

  def post(self, request):
    data = request.POST
    grade_form = self.form(data)
    if grade_form.is_valid():
      try:
        grade_form.save()
        messages.success(request, message="Grado creado con exito")
      except:
        messages.error(request, message="Error la base de datos")
    else:
      errors = [error for error in grade_form.errors.values()]
      messages.error(request, message=f"{errors[0][0]}")
    return redirect('grades')
  
  def put(self, request, grade_id):
    data = request.PUT
    instance = self.grades.get(pk=grade_id)
    grade_form = self.form(data, instance=instance)
    if grade_form.is_valid():
      try:
        grade_form.save()
        messages.success(request, message="Grado actualizado con exito")
      except:
        messages.error(request, message="Error la base de datos")
    else:
      errors = [error for error in grade_form.errors.values()]
      messages.error(request, message=f"{errors[0][0]}")
    return redirect('grades')


#MATERIAS
@method_decorator(login_required, name="dispatch")
class SubjectView(View):
  def __init__(self, *args, **kwargs):
    self.form = SubjectForm
    self.subjects = Subject.objects.all()

  @check_user_type
  def get(self, request, *args, **kwargs):
    user_group = kwargs.get("user_group")
    if "subject_id" in kwargs:
      if self.subjects.get(pk=kwargs["subject_id"]).delete():
        messages.info(request, message="Materia eliminada")
      else:
        messages.error(request, message="No se pudo eliminar la materia")
      return redirect('subjects')
    else:
      return render(
        request,
        "academic_data/subjects/subjects.html",
        {"subjects": self.subjects, "form": self.form, "user_group": user_group}
      )

  def post(self, request):
    data = dict(request.POST)
    data["name"] = data["name"][0].title() 
    subject_form = self.form(data)
    if subject_form.is_valid():
      try:
        subject_form.save()
        messages.success(request, "Materia creada")
      except:
        messages.error(request, "Error la base de datos")
    else:
      errors = [error for error in subject_form.errors.values()]
      messages.error(request, message=f"{errors[0][0]}")
    return redirect('subjects')
  
  def put(self, request, subject_id):
    data = dict(request.PUT)
    data["name"] = data["name"][0].title()
    instance = self.subjects.get(pk=subject_id)
    subject_form = self.form(data, instance=instance)
    if subject_form.is_valid():
      try:
        subject_form.save()
        messages.success(request, message="Materia actualizada con exito")
      except:
        messages.error(request, message="Error la base de datos")
    else:
      errors = [error for error in subject_form.errors.values()]
      messages.error(request, message=f"{errors[0][0]}")
    return redirect('subjects')


#PERIODO ACADEMICO
@method_decorator(login_required, name="dispatch")
class AcademicPeriodView(View):
  def __init__(self, *args, **kwargs):
    self.form = AcademicPeriodForm
    self.academic_periods = AcademicPeriod.objects.all()

  @check_user_type
  def get(self, request, *args, **kwargs):
    user_group = kwargs.get("user_group")
    if "academic_period_id" in kwargs:
      self.academic_periods.get(pk=kwargs["academic_period_id"]).delete()
      messages.info(request, message="Periodo academico eliminado")
      return redirect('academic-periods')
    else:
      return render(
        request,
        "academic_data/academic_periods/academic_periods.html",
        {"academic_periods": self.academic_periods, "form": self.form, "user_group": user_group}
      )

  def post(self, request):
    academic_period_form = self.form(request.POST)
    if academic_period_form.is_valid():
      try:
        academic_period_form.save()
        messages.success(request, message="Periodo academico creado con exito")
      except:
        messages.error(request, message="Error la base de datos")
    else:
      errors = [error for error in academic_period_form.errors.values()]
      messages.error(request, message=f"{errors[0][0]}")
    return redirect('academic-periods')
  
  def put(self, request, academic_period_id):
    instance = self.academic_periods.get(pk=academic_period_id)
    academic_period_form = self.form(request.PUT, instance=instance)
    if academic_period_form.is_valid():
      try:
        academic_period_form.save()
        messages.success(request, message="Periodo academico actualizado con exito")
      except:
        messages.error(request, message="Error la base de datos")
    else:
      errors = [error for error in academic_period_form.errors.values()]
      messages.error(request, message=f"{errors[0][0]}")
    return redirect('academic-periods')


#DOCENTES
@method_decorator(login_required, name="dispatch")
class TeacherListView(ListView):
  template_name = "academic_data/teachers/teachers_list.html"
  queryset = Teacher.objects.select_related("parish", "gender").prefetch_related("subjects")

  @check_user_type
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context


@method_decorator(login_required, name="dispatch")
class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "academic_data/teachers/teacher_form.html"
    success_url = reverse_lazy('teachers-list')

    @check_user_type
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_action"] = reverse('create-teacher')
        context["action"] = "REGISTRAR"
        context["countries"] = Country.objects.all()
        return context

    def form_valid(self, form):
        teacher = form.save()
        teacher.parish_id = self.request.POST.get("parish")
        teacher.save()
        messages.success(self.request, "Registro de docente exitoso")
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, "No se pudo registrar al docente")
        return super().form_invalid(form)


@method_decorator(login_required, name="dispatch")
class TeacherUpdateView(UpdateView):
  model = Teacher
  form_class = TeacherForm
  template_name = "academic_data/teachers/teacher_form.html"

  def get_object(self, queryset=None):
    return Teacher.objects.get(pk=self.kwargs.get("teacher_id"))

  @check_user_type
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    teacher = self.get_object()
    context["form_action"] = reverse('update-teacher', kwargs={"teacher_id": teacher.id})
    context["action"] = "ACTUALIZAR"
    context["countries"] = Country.objects.all()
    return context

  def post(self, request, *args, **kwargs):
    teacher = self.get_object()
    teacher_form = self.form_class(request.POST, instance=teacher)
    if teacher_form.is_valid():
      teacher_form.save()
      messages.success(request, "Informacion de docente actualizada")
      return redirect("teachers-list")
    else:
      messages.error(request, "No se pudo actualizar la informacion del docente")
      return render(request, self.template_name, {'form': teacher_form})


@login_required
def delete_teacher(request, teacher_id):
    if Teacher.objects.get(pk=teacher_id).delete():
      messages.info(request, "Registro de docente eliminado")
    return redirect("teachers-list")


#MATRICULAS
@method_decorator(login_required, name="dispatch")
class TuitionListView(ListView):
  template_name = "academic_data/tuitions/tuitions_list.html"
  queryset = Tuition.objects.select_related("academic_period", "grade", "section", "shift").prefetch_related("students")

  @check_user_type
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context


class TuitionDetailView(DetailView):
  model = Tuition
  template_name = "academic_data/tuitions/tuition_detail.html"

  def get_object(self, queryset=None):
    tuition_id = self.kwargs.get("tuition_id")
    data = AllNotes.objects.filter(matricula=tuition_id)

    try:
      self.info_tuition = data.distinct("matricula").values()[0]
    except:
      tuition = Tuition.objects.get(id=tuition_id)
      self.info_tuition = {
        "periodo": tuition.academic_period.period,
        "grado": tuition.grade.year,
        "seccion": tuition.section.group,
        "turno": tuition.shift.turn,
        "matricula": tuition.id
      }

    self.subjects = data.distinct("asignacion").order_by("asignacion").values_list("asignacion", flat=True)

    students = data.order_by("p_nombre", "s_nombre", "p_apellido", "s_apellido", "cedula", "asignacion")

    def full_name(student):
      return f"{student['p_nombre']} {student['s_nombre'] if student['s_nombre'] else ''} {student['p_apellido']} {student['s_apellido'] if student['s_apellido'] else ''}"

    self.unique_students = list(
      (students.distinct(
        "cedula", "p_nombre", "s_nombre", "p_apellido", "s_apellido")
      ).values()
    )

    for student in self.unique_students:
      student["full_name"] = full_name(student)

      qualifications = students.filter(student_id=student["student_id"])

      moment_1 = []
      moment_2 = []
      moment_3 = []

      for qualification in qualifications:
        note1 = "N/C"
        note2 = "N/C"
        note3 = "N/C"

        if qualification.momento1:
          note1 = qualification.momento1
        if qualification.momento2:
          note2 = qualification.momento2
        if qualification.momento3:
          note3 = qualification.momento3

        moment_1.append(note1)
        moment_2.append(note2)
        moment_3.append(note3)

      student["moment_1"] = moment_1
      student["moment_2"] = moment_2
      student["moment_3"] = moment_3

    return self.unique_students, self.info_tuition, self.subjects

  @check_user_type
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['subjects'] = self.subjects
    context['info_tuition'] = self.info_tuition
    context['unique_students'] = self.unique_students
    return context


@method_decorator(login_required, name="dispatch")
class TuitionCreateView(CreateView):
  model = Tuition
  form_class = TuitionForm
  template_name = "academic_data/tuitions/tuition_form.html"

  @check_user_type
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["form_action"] = reverse('create-tuition')
    context["action"] = "REGISTRAR"
    return context

  def post(self, request, *args, **kwargs):
    tuition_form = self.form_class(request.POST)
    if tuition_form.is_valid():
      tuition_form.save()
      messages.success(request, "Registro de matricula exitoso")
      return redirect("tuitions-list")
    else:
      messages.error(request, "No se pudo registrar la matricula")
      return render(request, self.template_name, {'form': tuition_form})


@method_decorator(login_required, name="dispatch")
class TuitionUpdateView(UpdateView):
  model = Tuition
  form_class = TuitionForm
  template_name = "academic_data/tuitions/tuition_form.html"

  def get_object(self, queryset=None):
    return Tuition.objects.get(pk=self.kwargs.get("tuition_id"))

  @check_user_type
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    tuition = self.get_object()
    context["form_action"] = reverse('update-tuition', kwargs={"tuition_id": tuition.id})
    context["action"] = "ACTUALIZAR"
    return context

  def post(self, request, *args, **kwargs):
    tuition = self.get_object()
    tuition_form = self.form_class(request.POST, instance=tuition)
    if tuition_form.is_valid():
      tuition_form.save()
      messages.success(request, "Informacion de matricula actualizada")
      return redirect("tuitions-list")
    else:
      messages.error(request, "No se pudo actualizar la informacion de la matricula")
      return render(request, self.template_name, {'form': tuition_form})


@login_required
def delete_tuition(request, tuition_id):
    if Tuition.objects.get(pk=tuition_id).delete():
      messages.info(request, "Registro de matricula eliminado")
    return redirect("tuitions-list")


#NOTAS
def upload_qualification_by_student(request):
  return render(request, "academic_data/qualifications/upload_by_student.html")


@check_user_type
@login_required
def upload_qualification_by_tuition(request, **kwargs):
  tuitions = Tuition.objects.prefetch_related(
    Prefetch(
        "students", queryset=Student.objects.order_by("first_name", "second_name", "first_surname", "second_surname")
      )
  )
  subjects = Subject.objects.all()
  moments = Moment.objects.all()

  context_data = {
    "tuitions": tuitions,
    "subjects": subjects,
    "moments": moments,
  }

  context_data.update(kwargs)

  if request.method == "GET":
    return render(request, "academic_data/qualifications/upload_by_tuition.html", context_data)
  elif request.method == "POST":
    tuition_id = request.POST.get("tuition")
    subject_id = request.POST.get("subject")
    moment_id = request.POST.get("moment")

    note_keys = [key for key in request.POST.keys() if key.startswith("note_")]

    bulk_list = []
    for note_key in note_keys:
      student_id = note_key.split("_")[1]
      note = request.POST[note_key]

      bulk_list.append(Qualification(
        student_id=student_id, tuition_id=tuition_id, subject_id=subject_id, moment_id=moment_id, note=note 
      ))
    Qualification.objects.bulk_update_or_create(bulk_list, ["note"], match_field=["student", "subject", "tuition", "moment"])

    return redirect(reverse("detail-tuition", kwargs={"tuition_id": tuition_id}))
    

#APIS#
@api_view(["GET"])
def tuition_detail_api(request, tuition_id, subject_id, moment_id):
  try:
    tuition = Tuition.objects.filter(pk=tuition_id).prefetch_related(
      Prefetch(
        "students", queryset=Student.objects.order_by("first_name").prefetch_related(
          Prefetch(
            "qualifications", queryset=Qualification.objects.filter(subject_id=subject_id, moment_id=moment_id, tuition_id=tuition_id)
          )
        )
      )
    )[0]
    serializer = TuitionSerializer(tuition)
    return Response(serializer.data)
  except Tuition.DoesNotExist as e:
    return Response({"msg": str(e)}, status=status.HTTP_404_NOT_FOUND)



#Reporte #1

def export_pdf(request, tuition_id, student_id):
  from datetime import datetime
  #model = Tuition
  
  data = AllNotes.objects.filter(student_id=student_id, matricula=tuition_id)
  context = {}
  context['id'] = student_id 
  context['all'] = data[0]
  context['asignaciones'] = [item for item in data.order_by("asignacion")]

  html = render_to_string("academic_data/tuitions/report-pdf.html", context)
  response = HttpResponse(content_type="application/pdf")
  response["Content-Disposition"] = "inline: report.pdf"
  font_config = FontConfiguration()
  HTML(string=html, base_url=request.build_absolute_uri() ).write_pdf(response,font_config=font_config)

  return response


def report_html(request,student_id):
    data = AllNotes.objects.filter(student_id=student_id)
    context = {}
    context['id'] = student_id 
    context['all'] = data[0]
    context['asignaciones'] = [item for item in data]
    template_name = "academic_data/tuitions/report-pdf.html"
    return render(request, template_name,context)

def report_constancia(request,student_id):
  data = AllNotes.objects.filter(student_id=student_id)
  context = {}
  context['id'] = student_id 
  context['all'] = data[0]

  #Codigo para convertir las fecha numerica en letras, quizas se puede reducir mucho mas pero esto es lo que pude hacer
  fecha = datetime.now()
  dia = fecha.day
  mes = fecha.month
  ano = int(str(fecha.year)[-2:])

  if dia == 1:
      dia = 'un'
  elif dia == 2:
      dia = 'dos'
  elif dia == 3:
      dia = 'tres'
  elif dia == 4:
      dia = 'cuatro'
  elif dia == 5:
      dia = 'cinco'
  elif dia == 6:
      dia = 'seis'
  elif dia == 7:
      dia = 'siete'
  elif dia == 8:
      dia = 'ocho'
  elif dia == 9:
      dia = 'nueve'
  elif dia == 10:
      dia = 'diez'
  elif dia == 11:
      dia = 'once'
  elif dia == 12:
      dia = 'doce'
  elif dia == 13:
      dia = 'trece'
  elif dia == 14:
      dia = 'catorce'
  elif dia == 15:
      dia = 'quince'
  elif dia == 16:
      dia = 'diez y seis'
  elif dia == 17:
      dia = 'diez y siete'
  elif dia == 18:
      dia = 'diez y ocho'
  elif dia == 19:
      dia = 'diez y nueve'
  elif dia == 20:
      dia = 'veinte'
  elif dia == 21:
      dia = 'veinte y uno'
  elif dia == 22:
      dia = 'veinte y dos'
  elif dia == 23:
      dia = 'veinte y tres'
  elif dia == 24:
      dia = 'veinte y cuatro'
  elif dia == 25:
      dia = 'veinte y cinco'
  elif dia == 26:
      dia = 'veinte y seis'
  elif dia == 27:
      dia = 'veinte y siete'
  elif dia == 28:
      dia = 'veinte y ocho'
  elif dia == 29:
      dia = 'veinte y nueve'
  elif dia == 30:
      dia = 'treinta'
  elif dia == 31:
      dia = 'treinta y uno'

  meses = {
    1: 'enero',
    2: 'febrero',
    3: 'marzo',
    4: 'abril',
    5: 'mayo',
    6: 'junio',
    7: 'julio',
    8: 'agosto',
    9: 'septiembre',
    10: 'octubre',
    11: 'noviembre',
    12: 'diciembre'
  }
  mes = meses.get(mes, '')

  anos = {
    24: 'veinte y cuatro',
    25: 'veinte y cinco',
    26: 'veinte y seis',
    27: 'veinte y siete',
    28: 'veinte y ocho',
    29: 'veinte y nueve',
    30: 'treinta',
    31: 'treinta y uno',
    32: 'treinta y dos',
    33: 'treinta y tres',
    34: 'treinta y cuatro'
  }
  ano = anos.get(ano, '')

  context['dia'] = dia
  context['mes'] = mes
  context['ano'] = ano
  #print(f'{dia} de {mes} del ano dos mil {ano}')

  html = render_to_string("academic_data/tuitions/proof-of-studies.html", context)
  response = HttpResponse(content_type="application/pdf")
  response["Content-Disposition"] = "inline: report.pdf"
  font_config = FontConfiguration()
  HTML(string=html, base_url=request.build_absolute_uri() ).write_pdf(response,font_config=font_config)
  #template_name = "academic_data/tuitions/proof-of-studies.html"
  #return render(request, template_name,context)
  return response
