from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('Date Published')
    
    def __str__(self):
        return self.title
    







