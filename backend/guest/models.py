from django.db import models

# Create your models here.

class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"