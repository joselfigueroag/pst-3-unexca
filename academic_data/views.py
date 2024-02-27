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
from students.models import Student
from .models import Section, Grade, Subject, Teacher, AcademicPeriod, Tuition, Qualification, AllNotes
from .forms import SectionForm, GradeForm, SubjectForm, TeacherForm, AcademicPeriodForm, TuitionForm
from .serializers import TuitionSerializer

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration


#SECCIONES
@method_decorator(login_required, name="dispatch")
class SectionView(View):
  def __init__(self, *args, **kwargs):
    self.form = SectionForm
    self.sections = Section.objects.all()

  def get(self, request, *args, **kwargs):
    if "section_id" in kwargs:
      self.sections.get(pk=kwargs["section_id"]).delete()
      messages.info(request, message="Seccion eliminada")
      return redirect('sections')
    else:
      return render(
        request,
        "academic_data/sections/sections.html",
        {"sections": self.sections, "form": self.form}
      )

  def post(self, request):
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

  def get(self, request, *args, **kwargs):
    if "grade_id" in kwargs:
      self.grades.get(pk=kwargs["grade_id"]).delete()
      messages.info(request, message="Grado eliminado")
      return redirect('grades')
    else:
      return render(
        request,
        "academic_data/grades/grades.html",
        {"grades": self.grades, "form": self.form}
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

  def get(self, request, *args, **kwargs):
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
        {"subjects": self.subjects, "form": self.form}
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
      errors = [error for error in grade_form.errors.values()]
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

  def get(self, request, *args, **kwargs):
    if "academic_period_id" in kwargs:
      self.academic_periods.get(pk=kwargs["academic_period_id"]).delete()
      messages.info(request, message="Periodo academico eliminado")
      return redirect('academic-periods')
    else:
      return render(
        request,
        "academic_data/academic_periods/academic_periods.html",
        {"academic_periods": self.academic_periods, "form": self.form}
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


@method_decorator(login_required, name="dispatch")
class TeacherCreateView(CreateView):
  model = Teacher
  form_class = TeacherForm
  template_name = "academic_data/teachers/teacher_form.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["form_action"] = reverse('create-teacher')
    context["action"] = "REGISTRAR"
    context["countries"] = Country.objects.all()
    return context

  def post(self, request, *args, **kwargs):
    teacher_form = self.form_class(request.POST)
    if teacher_form.is_valid():
      teacher = teacher_form.save()
      teacher.parish_id = request.POST.get("parish")
      teacher.save()
      messages.success(request, "Registro de docente exitoso")
      return redirect("teachers-list")
    else:
      messages.error(request, "No se pudo registrar al docente")
      return render(request, self.template_name, {'form': teacher_form})


@method_decorator(login_required, name="dispatch")
class TeacherUpdateView(UpdateView):
  model = Teacher
  form_class = TeacherForm
  template_name = "academic_data/teachers/teacher_form.html"

  def get_object(self, queryset=None):
    return Teacher.objects.get(pk=self.kwargs.get("teacher_id"))

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


class TuitionDetailView(DetailView):
  model = Tuition
  template_name = "academic_data/tuitions/tuition_detail.html"

  def get_object(self, queryset=None):
    tuition_id = self.kwargs.get("tuition_id")
    data = AllNotes.objects.filter(matricula=tuition_id)

    students = data.distinct("cedula")
    self.students = list(students.values())

    def full_name(student):
      return f"{student['p_nombre']} {student['s_nombre'] if student['s_nombre'] else ''} {student['p_apellido']} {student['s_apellido'] if student['s_apellido'] else ''}"

    for student in self.students:
      student["full_name"] = full_name(student)
    
    self.info_tuition = data.distinct("matricula").values()[0]

    # self.tuition = Tuition.objects.filter(pk=tuition_id).prefetch_related(
    #   Prefetch(
    #     "students",
    #     queryset=Student.objects.order_by("first_name").prefetch_related(
    #       Prefetch(
    #         "qualifications",
    #         queryset=Qualification.objects.filter(tuition_id=tuition_id).order_by("subject__name"),
    #         to_attr="all_qualifications"
    #       )
    #     ),
    #     to_attr="all_students",
    #   ),
    # )[0]

    # for student in self.tuition.all_students:
    #   student.moment_1 = [Decimal(0.0)]
    #   student.moment_2 = [Decimal(0.0)]
    #   student.moment_3 = [Decimal(0.0)]

    #   # Iterar sobre las calificaciones de cada estudiante
    #   for qualification in student.all_qualifications:
    #       # Asignar la nota a su momento correspondiente si no se ha asignado antes
    #       if qualification.moment_id == 1 and len(student.moment_1) == 1:
    #           student.moment_1[0] = qualification.note
    #       elif qualification.moment_id == 2 and len(student.moment_2) == 1:
    #           student.moment_2[0] = qualification.note
    #       elif qualification.moment_id == 3 and len(student.moment_3) == 1:
    #           student.moment_3[0] = qualification.note
    #     # student.moment_1 = []
    #     # student.moment_2 = []
    #     # student.moment_3 = []
      
    #   # for qualification in student.all_qualifications:
    #   #   moment1 = Decimal(0.0)
    #   #   moment2 = Decimal(0.0)
    #   #   moment3 = Decimal(0.0)

    #   #   if qualification.moment_id == 1:
    #   #     moment1 = qualification.note
    #   #   elif qualification.moment_id == 2:
    #   #     moment2 = qualification.note
    #   #   elif qualification.moment_id == 3:
    #   #     moment3 = qualification.note

    #   #   student.moment_1.append(moment1)
    #   #   student.moment_2.append(moment2)
    #   #   student.moment_3.append(moment3)
    
    # self.subjects = Subject.objects.filter(qualifications__tuition_id=tuition_id).distinct()
    return students, self.info_tuition

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # context['subjects'] = self.subjects
    context['info_tuition'] = self.info_tuition
    context['students'] = self.students
    return context


@method_decorator(login_required, name="dispatch")
class TuitionCreateView(CreateView):
  model = Tuition
  form_class = TuitionForm
  template_name = "academic_data/tuitions/tuition_form.html"

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


def upload_qualification_by_tuition(request):
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

def export_pdf(request,student_id):
  from datetime import datetime
  #model = Tuition
  
  data = AllNotes.objects.filter(student_id=student_id)
  context = {}
  context['id'] = student_id 
  context['all'] = data[0]
  context['asignaciones'] = [item for item in data]

  html = render_to_string("academic_data/tuitions/report-pdf.html", context)
  response = HttpResponse(content_type="application/pdf")
  response["Content-Disposition"] = "inline: report.pdf"
  font_config = FontConfiguration()
  HTML(string=html, base_url=request.build_absolute_uri() ).write_pdf(response,font_config=font_config)

  return response


def report_html(request,student_id):
    model = Tuition
    data = AllNotes.objects.filter(matricula=student_id)
    template_name = "academic_data/tuitions/report-pdf.html"
    return render(request, template_name)
