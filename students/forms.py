from django import forms

from .models import Student, AdditionalStudentData, Representative


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = [
      "first_name",
      "second_name",
      "first_surname",
      "second_surname",
      "birthday_date",
      "gender",
      "identity_card",
    ]


class AdditionalStudentDataForm(forms.ModelForm):
  class Meta:
    model = AdditionalStudentData
    fields = [
      "size",
      "weight",
      "email",
      "phone_number",
    ]


class RepresentativeForm(forms.ModelForm):
  class Meta:
    model = Representative
    fields = [
      "first_name",
      "second_name",
      "first_surname",
      "second_surname",
      "identity_card",
      "email",
      "phone_number",
    ]
