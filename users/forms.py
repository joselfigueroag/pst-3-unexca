from django import forms
from django.contrib.auth.models import Group
from .models import User


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "password", "group",)

    # email = forms.EmailField(max_length=200, required=True)
    # group = forms.ModelChoiceField(queryset=Group.objects.values_list("name", flat=True),)
    # password = forms.PasswordInput(render_value=False)

