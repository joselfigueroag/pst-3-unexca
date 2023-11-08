from django import forms
from django.contrib.auth.models import Group

from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    # def __init__(self, *args, **kwargs):
    #   super().__init__(*args, **kwargs)
    #   if 'instance' in kwargs:
    #     self.fields['password'].required = False

    class Meta:
      model = User
      fields = ["email", "group", "password"]
    
    def save(self, commit=True):
      user = super().save(commit=False)
      user.set_password(self.cleaned_data["password"])
      if commit:
        user.save()
    
      return user
