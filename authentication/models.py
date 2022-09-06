from django.db import models

# Create your models here.

class Student_model(models.Model):
    name =      models.CharField(max_length=100)
    email =     models.EmailField()
    sem =       models.IntegerField()
    is_active = models.BooleanField()   #BY DEFAULT IT IS FALSE
    doc =       models.FileField(upload_to='')
    def __str__(self):
        return self.name