from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    dis  = models.TextField()
    price = models.IntegerField(default=0)
    uniqueID = models.CharField(max_length=10, blank=True)
    img = models.TextField()
    
    def __str__(self):
        return self.name
    

class Service(models.Model):
    name = models.CharField(max_length=50)
    dis = models.TextField()
    minPrice = models.IntegerField()
    maxPrice = models.IntegerField()
    img = models.TextField()
    
    def __str__(self):
        return self.name