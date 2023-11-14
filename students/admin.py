from django.contrib import admin
from django import forms

from .models import Student, Representative, AdditionalStudentData

#revisar
# class RepresentativeInlineFormSet(forms.models.BaseInlineFormSet):
#   def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     # Puedes personalizar la apariencia de los campos aquí, por ejemplo:
#     for form in self.forms:
#         form.fields['first_name'].widget.attrs['style'] = 'display:block;'
#         form.fields['second_name'].widget.attrs['style'] = 'display:block;'
#         form.fields['first_surname'].widget.attrs['style'] = 'display:block;'
#         form.fields['second_surname'].widget.attrs['style'] = 'display:block;'
#         form.fields['identity_card'].widget.attrs['style'] = 'display:block;'
#         form.fields['email'].widget.attrs['style'] = 'display:block;'
#         form.fields['phone_number'].widget.attrs['style'] = 'display:block;'


class AdditionalStudentDataInline(admin.TabularInline):
  model = AdditionalStudentData
  extra = 0


class RepresentativeInline(admin.TabularInline):
  model = Representative
  extra = 0
  # formset = RepresentativeInlineFormSet


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  inlines = [AdditionalStudentDataInline]


@admin.register(Representative)
class RepresentativeAdmin(admin.ModelAdmin):
  pass
