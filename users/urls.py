from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    logout_view,
    UserListView,
    NewUserView,
    register_user,
    EditUserView,
    update_user,
)


urlpatterns = [
    path(
        "",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", logout_view, name="logout"),
    path("user-list/", UserListView.as_view(), name="user-list"),
    path("new-user/", NewUserView.as_view(), name="new-user"),
    path("register-user/", register_user, name="register-user"),
    path("edit-user/<int:id>/", EditUserView.as_view(), name="edit-user"),
    path("update-user/<int:id>/", update_user, name="update-user"),
]
