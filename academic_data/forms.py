from django import forms

from .models import Section, Grade, Subject, Teacher


class SectionForm(forms.ModelForm):
  class Meta:
    model = Section
    fields = ["group"]


class GradeForm(forms.ModelForm):
  class Meta:
    model = Grade
    fields = ["year", "sections"]


class SubjectForm(forms.ModelForm):
  class Meta:
    model = Subject
    fields = ["name"]


class TeacherForm(forms.ModelForm):
  class Meta:
    model = Teacher
    fields = [
      "first_name",
      "second_name",
      "first_surname",
      "second_surname",
      "birthday_date",
      "gender",
      "identity_card",
      "email",
      "phone_number",
      "subjects",
      "start_date",
      "status",
      "address",
    ]
