from django.db import models

# Create your models here.

class City(models.Model):
    city_name= models.CharField(max_length=100)
    discription= models.TextField()
    
