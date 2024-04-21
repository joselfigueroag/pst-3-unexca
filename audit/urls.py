from django.urls import path

from .views import (
  AuditListView,
)

urlpatterns = [
  path("audit_records/", AuditListView.as_view(), name="audit"),
]
