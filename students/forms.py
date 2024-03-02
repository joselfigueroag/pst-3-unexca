from django import forms
from django.forms import widgets
from django_select2 import forms as s2forms
import re
from .models import Student, AdditionalStudentData, Representative

NUMBER = r"^\d+$"
LETTERS_SPACES = r"^[a-zA-Z\s]+$"
LETTERS = r"^[a-zA-Z]+$"

class RepresentativeWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "first_name__icontains",
        "identity_card__icontains",
    ]


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
      "representative",
    ]
    widgets = {
      "birthday_date": widgets.DateInput(attrs={"type": "date", "class": "datepicker"}, format="%Y-%m-%d"),
      "representative": RepresentativeWidget,
    }
  def __init__(self, *args, **kwargs):
    super(StudentForm, self).__init__(*args, **kwargs)
    self.fields["first_name"].widget.attrs["pattern"] = "[A-Za-z ]{1,50}"
    self.fields["second_name"].widget.attrs["pattern"] = "[A-Za-z ]{1,50}"
    self.fields["first_surname"].widget.attrs["pattern"] = "[A-Za-z ]{1,50}"
    self.fields["second_surname"].widget.attrs["pattern"] = "[A-Za-z ]{1,50}"
    self.fields["identity_card"].widget.attrs["pattern"] = "[0-9]{8,10}" 

  def clean_field(self, field_name, type):
    field_value = self.cleaned_data.get(field_name)
    if field_value is None:
      return None 
    if type == "alpha" :
      if not re.match(LETTERS_SPACES,field_value):
        raise forms.ValidationError("Solo se permiten letras.")
    if type == "num":
      if not field_value.isdigit():
        raise forms.ValidationError("Solo se permiten numeros.")
      if len(field_value) < 8:
         raise forms.ValidationError("La cedula debe ser no menor de 8 digitos")
    return field_value.upper()
  
  def clean_first_name(self):
    return self.clean_field("first_name","alpha")
  
  def clean_second_name(self):
    return self.clean_field("second_name","alpha")
  
  def clean_first_surname(self):
    return self.clean_field("first_surname","alpha")
  
  def clean_second_surname(self):
    return self.clean_field("second_surname","alpha")
  
  def clean_identity_card(self):
    return self.clean_field("identity_card","num")

class AdditionalStudentDataForm(forms.ModelForm):
  class Meta:
    model = AdditionalStudentData
    fields = [
      "size",
      "weight",
      "email",
      "phone_number",
    ]
  def clean_field(self, field_name):
    field_value = self.cleaned_data.get(field_name)
    if field_value is None:
      return None 
    if not field_value.isdigit():
      raise forms.ValidationError("Solo se permiten numeros.")
    if len(field_value) < 11:
         raise forms.ValidationError("El telefono debe ser no menor de 11 digitos")
    return field_value.upper()
  
  def clean_phone_number(self):
    return self.clean_field("phone_number")
  

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
  def clean_field(self, field_name, type):
    field_value = self.cleaned_data.get(field_name)
    if field_value is None:
      return None 
    if type == "alpha" :
      if not re.match(LETTERS_SPACES,field_value):
        raise forms.ValidationError("Solo se permiten letras.")
    if type == "num":
      if not field_value.isdigit():
        raise forms.ValidationError("Solo se permiten numeros.")
      if len(field_value) < 8:
         raise forms.ValidationError("La cedula debe ser no menor de 8 digitos")
    return field_value.upper()
  
  def clean_first_name(self):
    return self.clean_field("first_name","alpha")
  
  def clean_second_name(self):
    return self.clean_field("second_name","alpha")
  
  def clean_first_surname(self):
    return self.clean_field("first_surname","alpha")
  
  def clean_second_surname(self):
    return self.clean_field("second_surname","alpha")
  
  def clean_identity_card(self):
    return self.clean_field("identity_card","num")
  
  def clean_phone_number(self):
    return self.clean_field("phone_number","num")