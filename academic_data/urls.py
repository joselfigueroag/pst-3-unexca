from django.urls import path

from .views import SectionView, GradeView, SubjectView

urlpatterns = [
  path("sections/", SectionView.as_view(), name="sections"),
  path("sections/<int:section_id>/", SectionView.as_view(), name="section"),
  path("grades/", GradeView.as_view(), name="grades"),
  path("grades/<int:grade_id>/", GradeView.as_view(), name="grade"),
  path("subjects/", SubjectView.as_view(), name="subjects"),
  path("subjects/<int:subject_id>/", SubjectView.as_view(), name="subject"),
]
