import re
from django import forms
from django.forms import widgets

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button
from django_select2 import forms as s2forms

from .models import Section, Grade, Subject, Teacher, AcademicPeriod, Tuition
from students.models import Student


NUMBER = r"^\d+$"
LETTERS_SPACES = r"^[a-zA-ZñÑ\s]+$"
LETTERS = r"^[a-zA-ZñÑ]+$"

class SectionForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["group"].widget.attrs.update({
      "pattern": "[A-Za-z]",
      "placeholder": "Ej: A",
    })

  class Meta:
    model = Section
    fields = ["group"]
  
  def clean_group(self):
    group = self.cleaned_data.get("group")
    if not re.match(LETTERS, group):
      raise forms.ValidationError("Solo se permiten letras.")

    return group.upper()


class GradeForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["year"].widget.attrs.update({
      "placeholder": "Ej: 1er",
    })

  class Meta:
    model = Grade
    fields = ["year", "subjects"]


class SubjectForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["name"].widget.attrs.update({
      "placeholder": "Ej: Matematica",
    })

  class Meta:
    model = Subject
    fields = ["name"]


class TeacherForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["first_name"].widget.attrs.update({
      "placeholder": "Ej: Juan",
    })

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
    widgets = {
      'birthday_date': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      'start_date': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    }

  def common_validation(self, field_name):
    value = self.cleaned_data.get(field_name)
    if value:
      if field_name == "identity_card":
        if not value.isdigit():
          raise forms.ValidationError("El numero de cedula solo puede contener digitos")
        if len(value) <= 7 :
          raise forms.ValidationError("La cedula debe ser no menor de 7 digitos")
      else:
        if not re.match(LETTERS_SPACES, value):
          raise forms.ValidationError("Solo puede contener letras y espacios")
        value = value.upper()
    
    return value

  def clean_identity_card(self):
    return self.common_validation("identity_card")

  def clean_first_name(self):
    return self.common_validation("first_name")

  def clean_second_name(self):
    return self.common_validation("second_name")
  
  def clean_first_surname(self):
    return self.common_validation("first_surname")

  def clean_second_surname(self):
    return self.common_validation("second_surname")


class AcademicPeriodForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["period"].widget.attrs.update({
            "pattern": "[0-9-]+",
            "placeholder": "Ej: 2023-2024",
        })

    class Meta:
        model = AcademicPeriod
        fields = ["period"]
  
    def clean_period(self):
        period = self.cleaned_data.get("period")
        if not re.match("[0-9-]+", period):
            raise forms.ValidationError("Solo se permiten números y el carácter '-'.")
        return period


class StudentMultipleWidget(s2forms.ModelSelect2MultipleWidget):
  search_fields = [
    "first_name__icontains",
    "first_surname__icontains",
    "identity_card__icontains",
  ]

  def build_attrs(self, base_attrs, extra_attrs=None):
    # Remove the "Delete All" button from the widget
    attrs = super().build_attrs(base_attrs, extra_attrs)
    attrs['data-allow-clear'] = 'false'
    return attrs


class TuitionForm(forms.ModelForm):
  class Meta:
    model = Tuition
    fields = ["academic_period", "grade", "section", "shift", "students"]
    widgets = {
      "students": StudentMultipleWidget,
    }

  def clean(self):
    try:
      academic_period = self.cleaned_data.get("academic_period")
      last_string = academic_period[-2]
      students = self.cleaned_data.get("students")

      students_ids = []
      tuitions = Tuition.objects.filter(academic_period__period__endswith=last_string).exclude(pk=self.instance.id)
      for tuition in tuitions:
        for student in tuition.students.all():
          students_ids.append(student.id)

      for student in students:
        if student.id in students_ids:
          raise forms.ValidationError(f"El almuno {student.full_name} se encuentra en otra matricula")
    except:
      pass
