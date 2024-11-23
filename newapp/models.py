from django.db import models

# Create your models here.
class  Feature(models.Model):
    
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    

class Team(models.Model):
    
    name = models.CharField(max_length=100)
    position  = models.CharField(max_length=80)
    image = models.ImageField(upload_to='images/',default='images/default.jpg')
    
