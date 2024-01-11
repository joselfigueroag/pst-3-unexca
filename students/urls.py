from django.urls import path, include

from .views import (
  StudentListView,
  StudentDetailView,
  StudentCreateView,
  StudentUpdateView,
  delete_student,
  RepresentativeListView,
  RepresentativeCreateView,
  RepresentativeUpdateView,
  delete_representative
)

urlpatterns = [
  path("students/", StudentListView.as_view(), name="students-list"),
  path("students/<int:student_id>", StudentDetailView.as_view(), name="detail-student"),
  path("students/create/", StudentCreateView.as_view(), name="create-student"),
  path("students/update/<int:student_id>/", StudentUpdateView.as_view(), name="update-student"),
  path("students/delete/<int:student_id>/", delete_student, name="delete-student"),
  path("representatives/", RepresentativeListView.as_view(), name="representatives-list"),
  path("representatives/create/", RepresentativeCreateView.as_view(), name="create-representative"),
  path("representatives/update/<int:representative_id>/", RepresentativeUpdateView.as_view(), name="update-representative"),
  path("representatives/delete/<int:representative_id>/", delete_representative, name="delete-representative"),
]