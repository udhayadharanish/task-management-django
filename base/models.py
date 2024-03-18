from django.db import models
from datetime import datetime

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('yet_to_start', 'Yet to Start'),
    )
    # user = 
    name = models.CharField(max_length=200,null=False)
    description = models.TextField(null=True,blank=True)
    notes = models.TextField(null=True,blank=True)
    deadline = models.DateTimeField(blank=False,default=datetime.now())
    stress = models.IntegerField(null=False)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,null=False)
    time = models.IntegerField(null=True)
    score = models.FloatField(null=False,default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-deadline','-stress']