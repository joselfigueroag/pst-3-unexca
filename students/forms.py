from django import forms
from django.forms import widgets
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
    widgets = {
      'birthday_date': widgets.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    }

  def __init__(self, *args, **kwargs):
    super(StudentForm, self).__init__(*args, **kwargs)
    self.fields['first_name'].widget.attrs['pattern'] = '[A-Za-z ]{1,50}'
    self.fields['second_name'].widget.attrs['pattern'] = '[A-Za-z ]{1,50}'
    self.fields['first_surname'].widget.attrs['pattern'] = '[A-Za-z ]{1,50}'
    self.fields['second_surname'].widget.attrs['pattern'] = '[A-Za-z ]{1,50}'
    self.fields['identity_card'].widget.attrs['pattern'] = '[0-9]{8,10}'


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
