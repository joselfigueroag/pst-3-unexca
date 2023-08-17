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
    birthday_date = models.DateField(verbose_name="fecha de nacimiento")
    gender = models.ForeignKey(Gender, models.PROTECT, related_name="students")
    identity_card = models.CharField(
        max_length=10, verbose_name="cedula de identidad", null=True, blank=True
    )

    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

    def __str__(self):
        return f"{self.first_name} {self.first_surname}"


class AdditionalStudentData(TimeStamp):
    student = models.ForeignKey(
        Student,
        models.CASCADE,
        verbose_name="estudiante",
        related_name="additional_data",
    )
    size = models.DecimalField(
        verbose_name="talla", max_digits=3, decimal_places=2, null=True, blank=True
    )
    weight = models.DecimalField(
        verbose_name="peso", max_digits=3, decimal_places=1, null=True, blank=True
    )
    email = models.EmailField(verbose_name="correo electronico", null=True, blank=True)
    phone_number = models.CharField(
        max_length=15, verbose_name="numero de telefono", null=True, blank=True
    )


class Representative(TimeStamp):
    student = models.ForeignKey(
        Student,
        models.CASCADE,
        verbose_name="estudiante",
        related_name="representatives",
    )
    first_name = models.CharField(max_length=50, verbose_name="primer nombre")
    second_name = models.CharField(
        max_length=50, verbose_name="segundo nombre", null=True, blank=True
    )
    first_surname = models.CharField(max_length=50, verbose_name="primer apellido")
    second_surname = models.CharField(
        max_length=50, verbose_name="segundo apellido", null=True, blank=True
    )
    identity_card = models.CharField(max_length=10, verbose_name="cedula de identidad")
    email = models.EmailField(verbose_name="correo electronico", null=True, blank=True)
    phone_number = models.CharField(
        max_length=15, verbose_name="numero de telefono", null=True, blank=True
    )
    address = models.CharField(max_length=200, verbose_name="direccion")

    class Meta:
        verbose_name = "representante"
        verbose_name_plural = "representantes"

    def __str__(self):
        return f"{self.first_name} {self.first_surname} - {self.student}"
