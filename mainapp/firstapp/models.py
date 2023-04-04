from django.db import models

# Create your models here.


class iNeuron(models.Model):
    course_name = models.CharField(max_length=30),
    course_id = models.IntegerField(),
    student_name = models.CharField(max_length=20)