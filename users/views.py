from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView

from .models import User
from .forms import UserForm
from common.views import check_user_type


class Login(LoginView):
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().get(request, *args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect("/")


@method_decorator(login_required, name="dispatch")
class UserListView(ListView):
    login_url = "/"
    template_name = "users/user_list.html"
    queryset = User.objects.prefetch_related("groups")

    @check_user_type
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required, name="dispatch")
class NewUserView(FormView):
    model = User
    form_class = UserForm
    template_name = "users/new_user.html"
    login_url = "/"

    @check_user_type
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@login_required
def register_user(request):
    user_form = UserForm(request.POST)
    if user_form.is_valid():
        user_form.save()
        messages.success(request, "Usuario registrado")
        return redirect("user-list")
    else:
        messages.error(request, "No se pudo registrar el usuario")
        return render(
            request,
            "users/new_user.html",
            {"form": user_form},
        )


@method_decorator(login_required, name="dispatch")
class EditUserView(FormView):
    model = User
    form_class = UserForm
    template_name = "users/edit_user.html"
    login_url = "/"

    def get_form(self, form_class=None):
        user = self.get_instance()
        user_form = self.form_class(instance=user)
        return user_form

    @check_user_type
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_id"] = self.get_instance().id
        return context

    def get_instance(self):
        return User.objects.get(pk=self.kwargs["id"])


@check_user_type
@login_required
def update_user(request, id):
    data = request.POST
    user = User.objects.get(pk=id)
    user.email = data["email"].lower()
    user.group_id = data["group"]
    user.save()
    return redirect("user-list")
