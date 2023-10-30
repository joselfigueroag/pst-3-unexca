from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Section, Grade, Subject
from .forms import SectionForm, GradeForm, SubjectForm

# Create your views here.

class SectionView(View):
  def __init__(self, *args, **kwargs):
    self.form = SectionForm()
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
    if "group" in data:
      Section.objects.create(group=data["group"])
    return redirect('sections')
  
  def put(self, request, section_id):
    data = request.PUT
    Section.objects.update_or_create(pk=self.kwargs["section_id"], defaults=data)
    return redirect('sections')

  def delete(self, request, section_id):
    self.sections.get(pk=section_id).delete()


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
      grade.sections.set(data["sections"])
    return redirect('grades')
  
  def put(self, request, grade_id):
    data = request.PUT
    sections = data.pop("sections")
    grade, created = Grade.objects.update_or_create(pk=self.kwargs["grade_id"], defaults=data)
    grade.sections.set(sections)
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
