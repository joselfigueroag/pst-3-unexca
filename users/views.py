from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
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
    queryset = User.objects.prefetch_related("groups")


class NewUserView(FormView):
    template_name = "users/new_user.html"
    model = User
    form_class = UserForm


def register_user(request):
    user_form = UserForm(request.POST)
    if user_form.is_valid():
        user_form.save()
        messages.success(request, "Usuario registrado")
        return redirect('user-list')
    else:
        messages.error(request, "No se pudo registrar el usuario")
        return render(
            request,
            "users/new_user.html",
            {"form": user_form},
        )


class EditUserView(FormView):
    template_name = "users/edit_user.html"
    model = User
    form_class = UserForm

    def get_form(self, form_class=None):
        user = self.get_instance()
        user_form = self.form_class(instance=user)
        return user_form
    
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
    # user = User.objects.get(pk=id)
    # user_form = UserForm(request.POST, instance=user)
    # if user_form.is_valid():
    #     user_form.save()
    #     messages.success(request, "Usuario actualizado")
    #     return redirect('user-list')
    # else:
    #     messages.error(request, "No se pudo actualizar el usuario")
    #     return render(
    #         request,
    #         "users/edit_user.html",
    #         {"form": user_form, "id": id},
    #     )
