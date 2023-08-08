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
        verbose_name_plural="paises"
        verbose_name="pais"
    def __str__(self) -> str:
        return f"{self.name}"

class State(TimeStamp):
    name = models.CharField(max_length=50, null=False)
    capital = models.CharField(max_length=50, null=True)
    country = models.ForeignKey(Country,on_delete=models.PROTECT)

class Municipality(TimeStamp):
    name = models.CharField(max_length=50, null=False)
    state = models.ForeignKey(State,on_delete=models.PROTECT)

class Parish(TimeStamp):
    name = models.CharField(max_length=50, null=False)
    municipality = models.ForeignKey(Municipality,on_delete=models.PROTECT)