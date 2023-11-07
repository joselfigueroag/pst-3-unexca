import re
from django import forms
from django.forms import widgets

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button

from .models import Section, Grade, Subject, Teacher


NUMBER = r"^\d+$"
LETTERS_SPACES = r"^[a-zA-Z\s]+$"

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

  def clean_identity_card(self):
    identity_card = self.cleaned_data.get("identity_card")
    if not re.match(NUMBER, identity_card):
      raise forms.ValidationError("El numero de cedula solo puede contener digitos")

    return identity_card

  def clean_first_name(self):
    first_name = self.cleaned_data.get("first_name")
    if not re.match(LETTERS_SPACES, first_name):
      raise forms.ValidationError("Solo puede contener letras y espacios")
    first_name = first_name.upper()

    return first_name
