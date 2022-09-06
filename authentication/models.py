from django.db import models

# Create your models here.

class Student_data(models.Model):
    stu_dept = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.stu_dept

class Student_model(models.Model):
    dept =     models.ForeignKey(Student_data, on_delete=models.CASCADE)
    name =      models.CharField(max_length=100)
    email =     models.EmailField()
    sem =       models.IntegerField()
    is_active = models.BooleanField()   #BY DEFAULT IT IS FALSE
    doc =       models.FileField(upload_to='')
    def __str__(self):
        return self.name
