from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Section, Grade
from .forms import SectionForm, GradeForm

# Create your views here.

class SectionView(View):
  def __init__(self, *args, **kwargs):
    self.form = SectionForm()
    self.sections = Section.objects.order_by("group")

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
    self.grades = Grade.objects.order_by("year")

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
    data = request.POST
    if "year" in data:
      Grade.objects.create(year=data["year"])
    return redirect('grades')
  
  def put(self, request, grade_id):
    data = request.PUT
    Grade.objects.update_or_create(pk=self.kwargs["grade_id"], defaults=data)
    return redirect('grades')

  def delete(self, request, grade_id):
    self.grades.get(pk=grade_id).delete()
