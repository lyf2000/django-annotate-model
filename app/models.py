from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Course(models.Model):
    name = models.CharField(max_length=128)


class Tariff(models.Model):
    name = models.CharField(max_length=128)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)


class AcademicGroup(models.Model):
    name = models.CharField(max_length=128)
    students = models.ManyToManyField(User)
