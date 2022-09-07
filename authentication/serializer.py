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
    def to_representation(self, instance):
        rep = super(Student_serializer, self).to_representation(instance)
        rep['dept'] = instance.dept.stu_dept
        return rep

class Student_update_serializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Student_model
        fields = '__all__'
        # fields = ('id','name', 'email', 'sem', 'is_active', 'doc', 'dept')

    def to_representation(self, instance):
        rep = super(Student_update_serializer, self).to_representation(instance)
        rep['dept'] = instance.dept.stu_dept
        return rep