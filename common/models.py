from django.db import models


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(TimeStamp):
    name = models.CharField(max_length=50, null=False)

    class Meta:
        verbose_name = "pais"
        verbose_name_plural = "paises"

    def __str__(self) -> str:
        return f"{self.name}"


class State(TimeStamp):
    name = models.CharField(max_length=50, null=False)
    capital = models.CharField(max_length=50, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, related_name="states"
    )

    class Meta:
        verbose_name = "estado"
        verbose_name_plural = "estados"

    def __str__(self) -> str:
        return f"{self.name} - {self.capital}"


class Municipality(TimeStamp):
    name = models.CharField(max_length=50, null=False)
    state = models.ForeignKey(
        State, on_delete=models.PROTECT, related_name="municipalities"
    )

    class Meta:
        verbose_name = "municipio"
        verbose_name_plural = "municipios"

    def __str__(self) -> str:
        return f"{self.name}"


class Parish(TimeStamp):
    name = models.CharField(max_length=50, null=False)
    municipality = models.ForeignKey(
        Municipality, on_delete=models.PROTECT, related_name="parroquia"
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
