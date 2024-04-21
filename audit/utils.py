from .models import Audit


def save_audit_record(user, action, model, description):
  Audit.objects.create(
    user=user,
    action=action,
    model=model,
    description=description
  )
