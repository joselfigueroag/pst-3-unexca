from django.urls import path, include

from .views import StudentListView, StudentCreateView, StudentUpdateView, delete_student

urlpatterns = [
  path("select2/", include("django_select2.urls")),
  path("", StudentListView.as_view(), name="students-list"),
  path("create/", StudentCreateView.as_view(), name="create-student"),
  path("update/<int:student_id>/", StudentUpdateView.as_view(), name="update-student"),
  path("delete/<int:student_id>/", delete_student, name="delete-student"),
]