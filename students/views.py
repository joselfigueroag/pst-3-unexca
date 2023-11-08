from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db import transaction

from .forms import StudentForm, AdditionalStudentDataForm, RepresentativeForm
from .models import Student, AdditionalStudentData, Representative


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
