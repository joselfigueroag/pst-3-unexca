from django.db import models


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(TimeStamp):
    name = models.CharField(max_length=50, verbose_name="nombre")

    class Meta:
        verbose_name = "pais"
        verbose_name_plural = "paises"

    def __str__(self) -> str:
        return f"{self.name}"


class State(TimeStamp):
    name = models.CharField(max_length=50, verbose_name="nombre")
    capital = models.CharField(max_length=50, verbose_name="capital", null=True)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, related_name="states", verbose_name="pais"
    )

    class Meta:
        verbose_name = "estado"
        verbose_name_plural = "estados"

    def __str__(self) -> str:
        return f"{self.name} - {self.capital}"


class Municipality(TimeStamp):
    name = models.CharField(max_length=50, verbose_name="nombre")
    state = models.ForeignKey(
        State,
        on_delete=models.PROTECT,
        related_name="municipalities",
        verbose_name="estado",
    )

    class Meta:
        verbose_name = "municipio"
        verbose_name_plural = "municipios"

    def __str__(self) -> str:
        return f"{self.name}"


class Parish(TimeStamp):
    name = models.CharField(max_length=50, verbose_name="nombre")
    municipality = models.ForeignKey(
        Municipality,
        on_delete=models.PROTECT,
        related_name="parishes",
        verbose_name="municipio",
    )

    class Meta:
        verbose_name = "parroquia"
        verbose_name_plural = "parroquias"

    def __str__(self) -> str:
        return f"{self.name}"


class Gender(models.Model):
    name = models.CharField(max_length=20, verbose_name="nombre")

    class Meta:
        verbose_name = "genero"
        verbose_name_plural = "generos"

    def __str__(self):
        return f"{self.name}"


class Shift(models.Model):
    turn = models.CharField(max_length=20, verbose_name="turno")

    class Meta:
        verbose_name = "jornada de estudio"
        verbose_name_plural = "jornadas de estudio"
    
    def __str__(self):
        return f"{self.turn}"


class Moment(models.Model):
    number = models.CharField(max_length=3, verbose_name="numero de momento")

    class Meta:
        verbose_name = "momento"
        verbose_name_plural = "momentos"
    
    def __str__(self):
        return f"{self.number} momento"
