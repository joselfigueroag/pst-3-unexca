from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import ListView, FormView

from .models import User
from .forms import UserForm

# Create your views here.


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class UserListView(ListView):
    template_name = "users/user_list.html"
    queryset = User.objects.all()


class NewUserView(FormView):
    template_name = "users/new_user.html"
    model = User
    form_class = UserForm


def register_user(request):
    data = request.POST
    user = User.objects.create(email=data["email"], group_id=data["group"])
    user.set_password(data["password"])
    user.save()
    return redirect('user-list')


class EditUserView(FormView):
    template_name = "users/edit_user.html"
    model = User
    form_class = UserForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        instance = self.get_instance()
        form.instance = instance
        form.fields['email'].initial = instance.email
        form.fields['group'].initial = instance.group.id if instance.group else ''
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.get_instance().id
        return context

    def get_instance(self):
        return User.objects.get(pk=self.kwargs['id'])


def update_user(request, id):
    data = request.POST
    user = User.objects.get(pk=id)
    user.email=data["email"]
    user.group_id=data["group"]
    user.save()

    return HttpResponseRedirect(reverse('user-list'))

