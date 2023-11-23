from django import forms
from django.contrib.auth.models import Group

from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
      model = User
      fields = ["email", "group", "password"]
    
    def clean_email(self):
      email = self.cleaned_data["email"]
      email = email.lower()
      return email

    def save(self, commit=True):
      user = super().save(commit=False)
      user.set_password(self.cleaned_data["password"])
      if commit:
        user.save()
      return user
