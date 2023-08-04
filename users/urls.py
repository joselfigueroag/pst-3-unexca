from django.urls import path
from django.contrib.auth import views as auth_views

from .views import logout_view, UserListView, CreateUserView


urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", logout_view, name="logout"),
    path("user-list/", UserListView.as_view(), name="user-list"),
    path("create-user/", CreateUserView.as_view(), name="create-user"),
]
