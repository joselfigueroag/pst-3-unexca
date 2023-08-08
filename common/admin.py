from django.contrib import admin
from .models import Country, State, Parish, Municipality

# Register your models here.
@admin.register(Country,State,Parish,Municipality)
class CountryAdmin(admin.ModelAdmin):
    fields=("name",)
class StateAdmin(admin.ModelAdmin):
    fields=('name','capital')
class ParishAdmin(admin.ModelAdmin):
    fields=('name',)
class MunicipalityAdmin(admin.ModelAdmin):
    fields=('name',)