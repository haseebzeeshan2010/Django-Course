from django.db import models

# Create your models here.

class Menu(models.Model): #In general one model is used per table
    name = models.CharField(max_length = 100) #create a table like this
    cuisine = models.CharField(max_length = 100) #charfield is used for strings
    price =  models.IntegerField()
