from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db import transaction

from .forms import StudentForm, AdditionalStudentDataForm, RepresentativeForm
from .models import Student, AdditionalStudentData, Representative


# ESTUDIANTES
class StudentListView(ListView):
  template_name = "students/students_list.html"
  queryset = Student.objects.select_related("additionalstudentdata", "gender")


class StudentCreateView(CreateView):
  template_name = "students/student_form.html"
  model = Student
  form_class = StudentForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["additional_info_form"] = AdditionalStudentDataForm
    context["form_action"] = reverse("create-student")
    return context

  @transaction.atomic
  def post(self, request, *args, **kwargs):
    student_form = self.form_class(request.POST)
    additional_form = AdditionalStudentDataForm(request.POST)
    if student_form.is_valid() and additional_form.is_valid():
        student = student_form.save()
        additional_data = additional_form.save(commit=False)
        additional_data.student = student
        additional_data.save()
        messages.success(request, "Registro de estudiante exitoso")
        return redirect("students-list")
    else:
        messages.error(request, "No se pudo registrar el estudiante")
        return render(
          request,
          self.template_name,
          {"form": student_form, "additional_info_form": additional_form }
        )


class StudentUpdateView(UpdateView):
  template_name = "students/student_form.html"
  model = Student
  form_class = StudentForm

  def get_object(self, queryset=None):
    return Student.objects.get(pk=self.kwargs.get("student_id"))

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    student = self.get_object()
    context["form_action"] = reverse("update-student", kwargs={"student_id": student.id})
    context["additional_info_form"] = AdditionalStudentDataForm(instance=student.additionalstudentdata)
    return context

  @transaction.atomic
  def post(self, request, *args, **kwargs):
    student = self.get_object()
    student_form = self.form_class(request.POST, instance=student)
    additional_form = AdditionalStudentDataForm(request.POST, instance=student.additionalstudentdata)
    if student_form.is_valid() and additional_form.is_valid():
      student = student_form.save()
      additional_data = additional_form.save(commit=False)
      additional_data.student = student
      additional_data.save()
      messages.success(request, "Registro de estudiante actualizado")
      return redirect("students-list")
    else:
      messages.error(request, "No se pudo actualizar registro del estudiante")
      return render(
        request,
        self.template_name,
        {"form": student_form, "additional_info_form": additional_form }
      )


def delete_student(request, student_id):
  if Student.objects.get(pk=student_id).delete():
    messages.info(request, "Registro de estudiante eliminado")
  return redirect("students-list")


#REPRESENTANTES
class RepresentativeListView(ListView):
  template_name = "representatives/representatives_list.html"
  queryset = Representative.objects.prefetch_related("students")


class RepresentativeCreateView(CreateView):
  template_name = "representatives/representative_form.html"
  model = Representative
  form_class = RepresentativeForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["form_action"] = reverse("create-representative")
    return context

  @transaction.atomic
  def post(self, request, *args, **kwargs):
    representative_form = self.form_class(request.POST)
    if representative_form.is_valid():
        representative_form.save()
        messages.success(request, "Registro de representante exitoso")
        return redirect("representatives-list")
    else:
        messages.error(request, "No se pudo registrar al representante")
        return render(
          request,
          self.template_name,
          { "form": representative_form }
        )


class RepresentativeUpdateView(UpdateView):
  template_name = "representatives/representative_form.html"
  model = Representative
  form_class = RepresentativeForm

  def get_object(self, queryset=None):
    return Representative.objects.get(pk=self.kwargs.get("representative_id"))

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    representative = self.get_object()
    context["form_action"] = reverse("update-representative", kwargs={"representative_id": representative.id})
    return context

  def post(self, request, *args, **kwargs):
    representative = self.get_object()
    representative_form = self.form_class(request.POST, instance=representative)
    if representative_form.is_valid():
      representative_form.save()
      messages.success(request, "Registro de representante actualizado")
      return redirect("representatives-list")
    else:
      messages.error(request, "No se pudo actualizar registro del representante")
      return render(
        request,
        self.template_name,
        { "form": representative_form }
      )


def delete_representative(request, representative_id):
  if Representative.objects.get(pk=representative_id).delete():
    messages.info(request, "Registro de representante eliminado")
  return redirect("representatives-list")

  