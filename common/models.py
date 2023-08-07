from django.db import models

# Create your models here.
class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Contries(TimeStamps):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)

class States(TimeStamps):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    contry_id = models.ForeignKey(Contries,on_delete=models.PROTECT)

class Municipalities(TimeStamps):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    state_id = models.ForeignKey(States,on_delete=models.PROTECT)

class Parishes(TimeStamps):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    Municipality_id = models.ForeignKey(Municipalities,on_delete=models.PROTECT)