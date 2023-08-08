from django.contrib import admin
from .models import Country, State, Parish, Municipality

# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields=("name",)