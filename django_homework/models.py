from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=32, null=False)
    surname = models.CharField(max_length=32, null=False)
