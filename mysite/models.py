from django.conf import settings
from django.db import models
from django.utils import timezone


class Journal(models.Model):
    name = models.CharField(max_length=200)


class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.CharField(max_length=50)


class StudentJournal(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)


class Topic(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, null=True)


class Mark(models.Model):
    mark = models.IntegerField(null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, null=True)
