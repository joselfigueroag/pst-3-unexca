from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import TimeStamp, Parish, Gender, Shift
from students.models import Student


class Subject(TimeStamp):
    name = models.CharField(max_length=50, verbose_name="nombre")

    class Meta:
        verbose_name = "materia"
        verbose_name_plural = "materias"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Teacher(TimeStamp):
    class Status(models.TextChoices):
        ACTIVE = "active", _("activo")
        INACTIVE = "inactive", _("inactivo")

    first_name = models.CharField(max_length=50, verbose_name="primer nombre")
    second_name = models.CharField(
        max_length=50, verbose_name="segundo nombre", null=True, blank=True
    )
    first_surname = models.CharField(max_length=50, verbose_name="primer apellido")
    second_surname = models.CharField(
        max_length=50, verbose_name="segundo apellido", null=True, blank=True
    )
    birthday_date = models.DateField(verbose_name="fecha de nacimiento", null=True)
    identity_card = models.CharField(max_length=10, verbose_name="cedula de identidad", unique=True)
    gender = models.ForeignKey(Gender, models.PROTECT, verbose_name="genero", related_name="teachers", null=True)
    email = models.EmailField(verbose_name="correo electronico", null=True, blank=True)
    phone_number = models.CharField(
        max_length=15, verbose_name="numero de telefono", null=True, blank=True
    )
    address = models.CharField(max_length=200, verbose_name="direccion")
    parish = models.ForeignKey(Parish, models.SET_NULL, null=True, verbose_name="parroquia")
    subjects = models.ManyToManyField(Subject, verbose_name="materias")
    start_date = models.DateField(verbose_name="fecha de inicio", null=True)
    status = models.CharField(max_length=10, verbose_name="estatus", choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        verbose_name = "docente"
        verbose_name_plural = "docentes"

    def __str__(self):
        return f"{self.first_name} {self.first_surname}"


class Section(TimeStamp):
    group = models.CharField(max_length=1, verbose_name="grupo", unique=True)

    class Meta:
        verbose_name = "seccion"
        verbose_name_plural = "secciones"
        ordering = ["group"]

    def __str__(self):
        return self.group


class Grade(TimeStamp):
    year = models.CharField(max_length=3, verbose_name="año", unique=True)

    class Meta:
        verbose_name = "grado"
        verbose_name_plural = "grados"
        ordering = ["year"]
    
    def __str__(self):
        return self.year


class AcademicPeriod(TimeStamp):
    period = models.CharField(max_length=9, verbose_name="periodo", unique=True)

    class Meta:
        verbose_name = "periodo academico"
        verbose_name_plural = "periodos academicos"
    
    def __str__(self):
        return self.period


class Tuition(TimeStamp):
    academic_period = models.ForeignKey(AcademicPeriod, models.CASCADE, verbose_name="periodo academico")
    grade = models.ForeignKey(Grade, models.CASCADE, verbose_name="grado")
    section = models.ForeignKey(Section, models.CASCADE, verbose_name="seccion")
    shift = models.ForeignKey(Shift, models.CASCADE, verbose_name="turno")
    students = models.ManyToManyField(Student, verbose_name="estudiantes", blank=True)

    class Meta:
        verbose_name = "matricula"
        verbose_name_plural = "matriculas"
        default_related_name = "tuitions"
        unique_together = ["academic_period", "grade", "section"]

    def __str__(self):
        return f"{self.academic_period} - {self.grade} {self.section}"


class Qualification(TimeStamp):
    student = models.ForeignKey(Student, models.CASCADE, verbose_name="estudiante")
    tuition = models.ForeignKey(Tuition, models.CASCADE, verbose_name="matricula")
    subject = models.ForeignKey(Subject, models.CASCADE, verbose_name="materia")
    note = models.DecimalField(verbose_name="nota", max_digits=3, decimal_places=1)

    class Meta:
        verbose_name = "calificacion"
        verbose_name_plural = "calificaciones"
        default_related_name = "qualifications"

    def __str__(self):
        return f"{self.student.full_name} - {self.subject.name} - {self.note}"
