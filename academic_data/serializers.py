from rest_framework import serializers

from .models import Tuition
from students.serializers import StudentSerializer


class TuitionSerializer(serializers.ModelSerializer):
  students = StudentSerializer(many=True, read_only=True)

  class Meta:
    model = Tuition
    depth = 1
    fields = "__all__"
