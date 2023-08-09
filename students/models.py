from django.db import models

from common.models import TimeStamp, Gender


# Create your models here.


class Student(TimeStamp):
    first_name = models.CharField(max_length=50, verbose_name="primer nombre")
    second_name = models.CharField(
        max_length=50, verbose_name="segundo nombre", null=True, blank=True
    )
    first_surname = models.CharField(max_length=50, verbose_name="primer apellido")
    second_surname = models.CharField(
        max_length=50, verbose_name="segundo apellido", null=True, blank=True
    )
    birthday_date = models.CharField(verbose_name="fecha de nacimiento")
    gender = models.ForeignKey(Gender, models.PROTECT, related_name="students")

    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

    def __str__(self):
        return f"{self.first_name} {self.first_surname}"
