from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question
    
class Answer(models.Model):
    answer = models.CharField(max_length=200)
    
    def __str__(self):
        return self.answer
    