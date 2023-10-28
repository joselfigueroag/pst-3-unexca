from django import forms

from .models import Section, Grade


class SectionForm(forms.ModelForm):
  class Meta:
    model = Section
    fields = ["group"]


class GradeForm(forms.ModelForm):
  class Meta:
    model = Grade
    fields = ["year"]
