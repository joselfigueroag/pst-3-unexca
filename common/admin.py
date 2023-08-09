from django.contrib import admin
from .models import Country, State, Parish, Municipality, Gender


# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ("name", "created_at")
    readonly_fields = ("created_at",)


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    fields = ("name", "capital")


@admin.register(Parish)
class ParishAdmin(admin.ModelAdmin):
    fields = ("name",)


@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    fields = ("name",)


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    pass
