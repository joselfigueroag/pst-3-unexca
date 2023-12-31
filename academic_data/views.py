from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from .models import Section, Grade, Subject, Teacher, AcademicPeriod, Tuition
from .forms import SectionForm, GradeForm, SubjectForm, TeacherForm, AcademicPeriodForm, TuitionForm


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
    return context

  def post(self, request, *args, **kwargs):
    teacher_form = self.form_class(request.POST)
    if teacher_form.is_valid():
      teacher_form.save()
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
