from django.db import models

from common.models import TimeStamp


class Teacher(TimeStamp):
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
        verbose_name = "docente"
        verbose_name_plural = "docentes"

    def __str__(self):
        return f"{self.first_name} {self.first_surname}"


class Subject(TimeStamp):
    name = models.CharField(max_length=50, verbose_name="nombre")

    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Section(TimeStamp):
    group = models.CharField(max_length=2, verbose_name="grupo")

    class Meta:
        verbose_name = "seccion"
        verbose_name_plural = "secciones"
        ordering = ["group"]

    def __str__(self):
        return self.group


class Grade(TimeStamp):
    year = models.CharField(max_length=3, verbose_name="año")
    sections = models.ManyToManyField(Section, verbose_name="secciones")

    class Meta:
        verbose_name = "grado"
        verbose_name_plural = "grados"
        ordering = ["year"]
    
    def __str__(self):
        sections = [section for section in self.sections.values_list("group", flat=True)]
        return f"{self.year} - {sections}"
