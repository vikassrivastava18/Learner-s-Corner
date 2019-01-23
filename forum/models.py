from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Topic(models.Model):
    topic = models.CharField(max_length=20)
    def __str__(self):
        return self.topic

class Question(models.Model):
   
    question = models.CharField(max_length=200, help_text='ask aquestion')
    asked_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True, blank=True,default=date.today())
    topic = models.ForeignKey('Topic',on_delete=models.SET_NULL, null=True)
    QUERY_STATUS = (
        ('p', 'Pending'),
        ('r', 'Resolved'),
    )
    
    status = models.CharField(max_length=1, choices=QUERY_STATUS, help_text='Status of Question Asked',default='p')

    def __str__(self):
        return '{0}'.format(self.question)

class Answer(models.Model):
    question = models.ForeignKey('Question',on_delete=models.SET_NULL, null=True)
    answer = models.CharField(max_length=400)
    answered_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True, blank=True,default=date.today())
    
    def __str__(self):
        return self.answer