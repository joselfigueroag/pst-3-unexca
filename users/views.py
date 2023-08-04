from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView


from .models import User
from .forms import CreateUserForm

# Create your views here.


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


class UserListView(ListView):
    template_name = "users/user_list.html"
    queryset = User.objects.all()

class CreateUserView(CreateView):
    template_name = "users/create_user.html"
    model = User
    form_class = CreateUserForm


# def create_user(request):
#     form = CreateUserForm(request.POST or None)
#     return render(request, "users/create_user.html", context={"form": form})

