from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import StudentForm, AdditionalStudentDataForm, RepresentativeForm
from .models import Student, AdditionalStudentData, Representative


class StudentListView(ListView):
  template_name = "students/students_list.html"
  queryset = Student.objects.all()


class StudentCreateView(CreateView):
  template_name = "students/create_student.html"
  model = Student
  form_class = StudentForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["additional_info_form"] = AdditionalStudentDataForm()
    context["representative_form"] = RepresentativeForm()
    return context

  def post(self, request, *args, **kwargs):
    data = dict(request.POST)
    student = Student.objects.create(
      first_name=data["first_name"][0],
      second_name=data["second_name"][0],
      first_surname=data["first_surname"][0],
      second_surname=data["second_surname"][0],
      birthday_date=data["birthday_date"][0],
      gender_id=data["gender"][0],
      identity_card=data["identity_card"][0],
    )

    AdditionalStudentData.objects.create(
      student=student,
      size=data["size"][0] if data["size"][0] else None,
      weight=data["weight"][0] if data["weight"][0] else None,
      email=data["email"][0],
      phone_number=data["phone_number"][0],
    )

    Representative.objects.create(
      student=student,
      first_name=data["first_name"][1],
      second_name=data["second_name"][1],
      first_surname=data["first_surname"][1],
      second_surname=data["second_surname"][1],
      identity_card=data["identity_card"][1],
      email=data["email"][1],
      phone_number=data["phone_number"][1],
    )

    return redirect("students-list")


class StudentUpdateView(UpdateView):
  template_name = "students/update_student.html"
  model = Student
  form_class = StudentForm

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    student = self.get_object()
    context["student_id"] = student.id
    context["additional_info_form"] = AdditionalStudentDataForm(instance=student.additionalstudentdata)
    context["representative_form"] = RepresentativeForm(instance=student.representative)
    return context

  def get_object(self, queryset=None):
    student_id = self.kwargs.get("student_id")
    return Student.objects.get(pk=student_id)

  def post(self, request, *args, **kwargs):
    data = dict(request.POST)
    student_id = self.kwargs["student_id"]

    student = Student.objects.get(pk=student_id)
    student.first_name = data["first_name"][0]
    student.second_name = data["second_name"][0]
    student.first_surname = data["first_surname"][0]
    student.second_surname = data["second_surname"][0]
    student.birthday_date = data["birthday_date"][0]
    student.gender_id = data["gender"][0]
    student.identity_card = data["identity_card"][0]
    student.save()

    additionalstudentdata = student.additionalstudentdata
    additionalstudentdata.size = data["size"][0] if data["size"][0] else None
    additionalstudentdata.weight = data["weight"][0] if data["weight"][0] else None
    additionalstudentdata.email = data["email"][0]
    additionalstudentdata.phone_number = data["phone_number"][0]
    additionalstudentdata.save()

    representative = student.representative
    representative.first_name=data["first_name"][1]
    representative.second_name=data["second_name"][1]
    representative.first_surname=data["first_surname"][1]
    representative.second_surname=data["second_surname"][1]
    representative.identity_card=data["identity_card"][1]
    representative.email=data["email"][1]
    representative.phone_number=data["phone_number"][1]
    representative.save()

    return redirect("students-list")


# class StudentDeleteView(DeleteView):
#   model = Student
#   success_url = reverse_lazy("students-list")
#   template_name = None

#   def get_object(self, queryset=None):
#     student_id = self.kwargs.get("student_id")
#     return Student.objects.get(pk=student_id)


def delete_student(request, student_id):
    Student.objects.get(pk=student_id).delete()
    return redirect("students-list")
