from django.db import models


from django.db import models

class Book(models.Model):
   title = models.CharField(max_length=100)
   author = models.CharField(max_length=100)
   year = models.IntegerField()
   price = models.DecimalField(max_digits=6, decimal_places=2)
   available = models.BooleanField(default=True)

   def __str__(self):
       return f"{self.title} ({self.author})"