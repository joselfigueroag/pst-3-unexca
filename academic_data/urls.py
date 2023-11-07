from django.urls import path

from .views import (
  SectionView,
  GradeView,
  SubjectView,
  TeacherListView,
  TeacherCreateView,
  TeacherUpdateView,
  delete_teacher,
)

urlpatterns = [
  path("sections/", SectionView.as_view(), name="sections"),
  path("sections/<int:section_id>/", SectionView.as_view(), name="section"),
  path("grades/", GradeView.as_view(), name="grades"),
  path("grades/<int:grade_id>/", GradeView.as_view(), name="grade"),
  path("subjects/", SubjectView.as_view(), name="subjects"),
  path("subjects/<int:subject_id>/", SubjectView.as_view(), name="subject"),
  path("teachers/", TeacherListView.as_view(), name="teachers-list"),
  path("teachers/create/", TeacherCreateView.as_view(), name="create-teacher"),
  path("teacher/update/<int:teacher_id>/", TeacherUpdateView.as_view(), name="update-teacher"),
  path("teacher/delete/<int:teacher_id>/", delete_teacher, name="delete-teacher"),
]
