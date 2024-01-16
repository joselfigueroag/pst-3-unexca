from django.urls import path, include

from .views import (
  SectionView,
  GradeView,
  SubjectView,
  AcademicPeriodView,
  TeacherListView,
  TeacherCreateView,
  TeacherUpdateView,
  delete_teacher,
  TuitionListView,
  TuitionDetailView,
  TuitionCreateView,
  TuitionUpdateView,
  delete_tuition,
  upload_qualification_by_student,
  upload_qualification_by_tuition,
  tuition_detail_api,
)

urlpatterns = [
  path("sections/", SectionView.as_view(), name="sections"),
  path("sections/<int:section_id>/", SectionView.as_view(), name="section"),
  path("grades/", GradeView.as_view(), name="grades"),
  path("grades/<int:grade_id>/", GradeView.as_view(), name="grade"),
  path("subjects/", SubjectView.as_view(), name="subjects"),
  path("subjects/<int:subject_id>/", SubjectView.as_view(), name="subject"),
  path("academic-periods/", AcademicPeriodView.as_view(), name="academic-periods"),
  path("academic-periods/<int:academic_period_id>/", AcademicPeriodView.as_view(), name="academic-period"),
  path("teachers/", TeacherListView.as_view(), name="teachers-list"),
  path("teachers/create/", TeacherCreateView.as_view(), name="create-teacher"),
  path("teacher/update/<int:teacher_id>/", TeacherUpdateView.as_view(), name="update-teacher"),
  path("teacher/delete/<int:teacher_id>/", delete_teacher, name="delete-teacher"),
  path("tuitions/", TuitionListView.as_view(), name="tuitions-list"),
  path("tuitions/<int:tuition_id>/", TuitionDetailView.as_view(), name="detail-tuition"),
  path("tuitions/create/", TuitionCreateView.as_view(), name="create-tuition"),
  path("tuition/update/<int:tuition_id>/", TuitionUpdateView.as_view(), name="update-tuition"),
  path("tuition/delete/<int:tuition_id>/", delete_tuition, name="delete-tuition"),
  path("qualification/upload-qualification-by-student/", upload_qualification_by_student, name="upload-qualification-by-student"),
  path("qualification/upload-qualification-by-tuition/", upload_qualification_by_tuition, name="upload-qualification-by-tuition"),
  path("api/tuition_detail_api/<int:id>/",  tuition_detail_api, name="tuition_detail_api"),
]
