from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from audit.models import Audit


@method_decorator(login_required, name="dispatch")
class AuditListView(ListView):
  template_name = "audit/records.html"
  queryset = Audit.objects.all()
