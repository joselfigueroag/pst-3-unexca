from rest_framework import serializers

from .models import Tuition, Qualification
from students.serializers import StudentSerializer


class QualificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Qualification
    fields = "__all__"


class TuitionSerializer(serializers.ModelSerializer):
  students = StudentSerializer(many=True, read_only=True)
  qualifications = QualificationSerializer(many=True)

  class Meta:
    model = Tuition
    depth = 1
    fields = "__all__"
