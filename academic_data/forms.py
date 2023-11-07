from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button

from .models import Section, Grade, Subject, Teacher


class SectionForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields["group"].widget.attrs.update({
      "pattern": "[A-Z]",
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
