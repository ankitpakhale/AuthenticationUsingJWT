from .models import *
from rest_framework import serializers

class Student_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_data
        fields = ('stu_dept')

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_model
        fields = '__all__'

class Student_update_serializer(serializers.ModelSerializer):
    # dept = serializers.CharField()
    id = serializers.IntegerField()
    dept = Student_data_serializer(many=True)
    class Meta:
        model = Student_model
        # fields = '__all__'
        fields = ('name', 'email', 'sem', 'is_active', 'doc', 'dept')
