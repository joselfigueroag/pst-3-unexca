from django import forms

from .models import Section, Grade, Subject


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
