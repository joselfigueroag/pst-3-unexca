from rest_framework import serializers

from .models import Country, State, Municipality, Parish


class CountrySerializer(serializers.ModelSerializer):
  class Meta:
    model = Country
    fields = ("id", "name", "states")

  class NestedStateSerializer(serializers.ModelSerializer):
    class Meta:
      model = State
      fields = ("id", "name",)

  states = NestedStateSerializer(many=True)


class StateSerializer(serializers.ModelSerializer):
  class Meta:
    model = State
    fields = ("id", "name", "capital", "municipalities")

  class NestedMunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
      model = Municipality
      fields = ("id", "name")
    
  municipalities = NestedMunicipalitySerializer(many=True)


class ParishSerializer(serializers.ModelSerializer):
  class Meta:
    model = Parish
    fields = ("id", "name")


class MunicipalitySerializer(serializers.ModelSerializer):
  parishes = ParishSerializer(many=True)

  class Meta:
    model = Municipality
    fields = ("id", "name", "parishes")
