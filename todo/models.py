from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(max_length=5000)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self): 
        return self.title