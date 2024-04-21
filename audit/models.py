from django.db import models

from users.models import User


class Audit(models.Model):
  user = models.ForeignKey(User, models.CASCADE, verbose_name="usuario", related_name="audits")
  action = models.CharField(max_length=50, verbose_name="accion")
  model = models.CharField(max_length=50, verbose_name="modelo afectado")
  description = models.CharField(max_length=100, verbose_name="descripcion", default=None)
  action_time = models.DateTimeField(verbose_name="fecha de accion", auto_now_add=True)

  class Meta:
    verbose_name_plural = "auditoria"
    ordering = ["-id"]