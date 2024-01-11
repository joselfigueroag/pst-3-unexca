from django.db import models

from common.models import TimeStamp, Gender


class Representative(TimeStamp):
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
    address = models.CharField(max_length=200, verbose_name="direccion", null=True)

    class Meta:
        verbose_name = "representante"
        verbose_name_plural = "representantes"

    def __str__(self):
        return f"{self.first_name} {self.first_surname} - {self.identity_card}"


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
    gender = models.ForeignKey(Gender, models.PROTECT, related_name="students", verbose_name="genero")
    identity_card = models.CharField(
        max_length=10, verbose_name="cedula de identidad", null=True, blank=True
    )
    representative = models.ForeignKey(
        Representative,
        models.CASCADE,
        null=True,
        verbose_name="representante",
        related_name="students",
    )

    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

    def __str__(self):
        return f"{self.first_name} {self.first_surname} - {self.identity_card if self.identity_card else ''}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.second_name if self.second_name else ''} {self.first_surname} {self.second_surname if self.second_surname else ''}" 


class AdditionalStudentData(TimeStamp):
    student = models.OneToOneField(
        Student,
        models.CASCADE,
        verbose_name="estudiante",
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

    class Meta:
        verbose_name = "informacion adicional del estudiante"
        verbose_name_plural = "informacion adicional de los estudiantes"
