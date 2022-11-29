from django.db import models

class item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0) #Dollars
    
    def __str__(self):
        return self.name

