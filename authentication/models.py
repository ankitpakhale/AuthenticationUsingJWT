from django.db import models

# Create your models here.

class Student_data(models.Model):
    stu_dept = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.stu_dept

class Student_model(models.Model):
    dept =     models.ForeignKey(Student_data, on_delete=models.CASCADE, null= True, blank=True)
    name =      models.CharField(max_length=100, null= True, blank=True)
    email =     models.EmailField(null= True, blank=True)
    sem =       models.IntegerField(null= True, blank=True)
    is_active = models.BooleanField(null= True, blank=True)   #BY DEFAULT IT IS FALSE
    doc =       models.FileField(upload_to='', null= True, blank=True)
    def __str__(self):
        return self.name