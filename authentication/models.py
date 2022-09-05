from django.db import models

# Create your models here.

class Student_model(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    sem=models.IntegerField()
    def __str__(self):
        return self.name