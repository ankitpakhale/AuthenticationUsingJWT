from .models import Student_model
from rest_framework import serializers

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_model
        fields = '__all__'

class Student_update_serializer(serializers.ModelSerializer):
    dept = serializers.CharField()
    id = serializers.IntegerField()
    class Meta:
        model = Student_model
        fields = '__all__'