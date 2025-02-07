from django.db import models

# Create your models here.
class product (models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True) 
    stock = models.PositiveIntegerField(default=0)
    
    def __str__ (self):
        return self.name

class cars (models.Model):
    name1 = models.CharField(max_length=100)  
    color1 =models.TextField()
    price1 = models.IntegerField()
    available1 = models.BooleanField(default=True)
    stock1 = models.PositiveIntegerField(default=0)
     
    