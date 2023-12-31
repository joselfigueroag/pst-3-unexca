import re
from django import forms
from django.forms import widgets

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button
from django_select2 import forms as s2forms

from .models import Section, Grade, Subject, Teacher, AcademicPeriod, Tuition
from students.models import Student


NUMBER = r"^\d+$"
LETTERS_SPACES = r"^[a-zA-Z\s]+$"
LETTERS = r"^[a-zA-Z]+$"

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
    fields = ["year"]


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
        if not re.match(NUMBER, value):
          raise forms.ValidationError("El numero de cedula solo puede contener digitos")
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
  class Meta:
    model = AcademicPeriod
    fields = ["period"]


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