from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
  full_name = serializers.SerializerMethodField()

  class Meta:
    model = Student
    fields = ("id", "full_name", "qualifications")
    ordering = ("first_name",)
    depth = 1

  def get_full_name(self, student):
    return student.full_name
