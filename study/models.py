from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Course(models.Model):
    subject = models.ForeignKey('Subject',on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Question(models.Model):
    course = models.ForeignKey('Course',on_delete=models.SET_NULL, null=True)
    question = models.CharField(max_length=2000)
    def __str__(self):
        return self.question

class Options(models.Model):
    question = models.ForeignKey('Question',on_delete=models.SET_NULL, null=True)
    option = models.CharField(max_length=200)
    def __str__(self):
        return self.option

class Answer(models.Model):
    question = models.ForeignKey('Question',on_delete=models.SET_NULL, null=True)
    answer =  models.CharField(max_length=200)
    def __str__(self):
        return self.answer
    
class Notes(models.Model):
    course = models.ForeignKey('Course',on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.CharField(max_length=10000)
    def __str__(self):
        return self.notes
