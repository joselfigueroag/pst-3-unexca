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

class StudentDetail(models.Model):
    student_id = models.IntegerField(primary_key=True, verbose_name="estudiante")
    sp_nombre = models.CharField(max_length=50, verbose_name="sp_nombre")
    ss_nombre = models.CharField(max_length=50, verbose_name="ss_nombre")
    sp_apellido = models.CharField(max_length=50, verbose_name="sp_apellido")
    ss_apellido = models.CharField(max_length=50, verbose_name="sp_apellido")
    s_cedula = models.CharField(max_length=50, verbose_name="s_cedula")
    genero = models.CharField(max_length=20, verbose_name="genero")
    peso = models.CharField(max_length=10, verbose_name="peso")
    talla = models.CharField(max_length=10, verbose_name="talla")
    tlf_stu = models.CharField(max_length=50, verbose_name="tlf_stu")
    rp_nombre = models.CharField(max_length=50, verbose_name="rp_nombre")
    rs_nombre = models.CharField(max_length=50, verbose_name="rs_nombre")
    rp_apellido = models.CharField(max_length=50, verbose_name="rp_apellido")
    rs_apellido = models.CharField(max_length=50, verbose_name="rs_apellido")
    r_cedula = models.CharField(max_length=50, verbose_name="r_cedula")
    tlf_rep = models.CharField(max_length=50, verbose_name="tlf_rep")
    r_correo = models.CharField(max_length=50, verbose_name="correo")
    periodo_id = models.CharField(max_length=50, verbose_name="periodo_id")
    periodo = models.CharField(max_length=50, verbose_name="periodo")
    ano = models.CharField(max_length=50, verbose_name="ano")
    seccion = models.CharField(max_length=50, verbose_name="seccion")

    class Meta:
        db_table = "student_detail_all"
        managed = False


