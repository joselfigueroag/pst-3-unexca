from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .models import Section, Grade, Subject, Teacher
from .forms import SectionForm, GradeForm, SubjectForm, TeacherForm

# Create your views here.

class SectionView(View):
  def __init__(self, *args, **kwargs):
    self.form = SectionForm
    self.sections = Section.objects.all()

  def get(self, request, *args, **kwargs):
    if "section_id" in kwargs:
      self.delete(request, kwargs["section_id"])
      return redirect('sections')
    else:
      return render(
        request,
        "academic_data/sections/sections.html",
        {"sections": self.sections, "form": self.form}
      )

  def post(self, request):
    data = request.POST
    section_form = self.form(data)
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
    data = request.PUT
    instance = self.sections.get(pk=section_id)
    section_form = self.form(data, instance=instance)
    if section_form.is_valid():
      section_form.save()
      messages.success(request, message="Seccion actualizada con exito")
    else:
      errors = [error for error in section_form.errors.values()]
      messages.error(request, message=f"{errors[0][0]}")
    return redirect('sections')

  def delete(self, request, section_id):
    messages.info(request, message="Seccion eliminada")
    self.sections.get(pk=section_id).delete()
  

# def delete_section(request, section_id):

#   self.sections.get(pk=section_id).delete()


class GradeView(View):
  def __init__(self, *args, **kwargs):
    self.form = GradeForm()
    self.grades = Grade.objects.all()

  def get(self, request, *args, **kwargs):
    if "grade_id" in kwargs:
      self.delete(request, kwargs["grade_id"])
      return redirect('grades')
    else:
      return render(
        request,
        "academic_data/grades/grades.html",
        {"grades": self.grades, "form": self.form}
      )

  def post(self, request):
    data = dict(request.POST)
    if "year" in data:
      grade = Grade.objects.create(year=data["year"][0])
    return redirect('grades')
  
  def put(self, request, grade_id):
    data = request.PUT
    grade, created = Grade.objects.update_or_create(pk=self.kwargs["grade_id"], defaults=data)
    return redirect('grades')

  def delete(self, request, grade_id):
    self.grades.get(pk=grade_id).delete()


class SubjectView(View):
  def __init__(self, *args, **kwargs):
    self.form = SubjectForm()
    self.subjects = Subject.objects.all()

  def get(self, request, *args, **kwargs):
    if "subject_id" in kwargs:
      self.delete(request, kwargs["subject_id"])
      return redirect('subjects')
    else:
      return render(
        request,
        "academic_data/subjects/subjects.html",
        {"subjects": self.subjects, "form": self.form}
      )

  def post(self, request):
    data = request.POST
    if "name" in data:
      Subject.objects.create(name=data["name"])
    return redirect('subjects')
  
  def put(self, request, subject_id):
    data = request.PUT
    Subject.objects.update_or_create(pk=self.kwargs["subject_id"], defaults=data)
    return redirect('subjects')

  def delete(self, request, subject_id):
    self.subjects.get(pk=subject_id).delete()


class TeacherListView(ListView):
  template_name = "academic_data/teachers/teachers_list.html"
  queryset = Teacher.objects.all()


class TeacherCreateView(CreateView):
  template_name = "academic_data/teachers/create_teacher.html"
  model = Teacher
  form_class = TeacherForm

  def post(self, request, *args, **kwargs):
    data = dict(request.POST)
    teacher = Teacher.objects.create(
      first_name=data["first_name"][0],
      second_name=data["second_name"][0],
      first_surname=data["first_surname"][0],
      second_surname=data["second_surname"][0],
      identity_card=data["identity_card"][0],
      gender_id=data["gender"][0],
      email=data["email"][0],
      phone_number=data["phone_number"][0],
    )
    teacher.subjects.set(data["subjects"])

    return redirect("teachers-list")


class TeacherUpdateView(UpdateView):
  template_name = "academic_data/teachers/update_teacher.html"
  model = Teacher
  form_class = TeacherForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    teacher = self.get_object()
    context["teacher_id"] = teacher.id
    return context

  def get_object(self, queryset=None):
    teacher_id = self.kwargs.get("teacher_id")
    return Teacher.objects.get(pk=teacher_id)

  def post(self, request, *args, **kwargs):
    data = dict(request.POST)
    teacher_id = self.kwargs["teacher_id"]

    teacher = Teacher.objects.get(pk=teacher_id)
    teacher.first_name = data["first_name"][0]
    teacher.second_name = data["second_name"][0]
    teacher.first_surname = data["first_surname"][0]
    teacher.second_surname = data["second_surname"][0]
    teacher.identity_card = data["identity_card"][0]
    teacher.gender_id = data["gender"][0]
    teacher.email = data["email"][0]
    teacher.phone_number = data["phone_number"][0]
    teacher.save()
    teacher.subjects.set(data["subjects"])

    return redirect("teachers-list")


def delete_teacher(request, teacher_id):
    Teacher.objects.get(pk=teacher_id).delete()
    return redirect("teachers-list")
