from django import forms
from django.contrib.auth.models import Group
from .models import User


# class BaseUserForm(forms.ModelForm):
#     class Meta:
#         model = User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
      model = User
      fields = ["email", "group", "password"]
      # fields = BaseUserForm.Meta.fields + ['password']
    