from dataclasses import fields
from .models import Student_model
from rest_framework import serializers


class Student_serializer(serializers.Serializer):
    class Meta:
        model = Student_model
        fields = '__all__'