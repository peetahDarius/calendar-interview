from django.db import models
from guest.models import Guest

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    label = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    all_day = models.BooleanField(default=False)  
    event_url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100)
    description = models.TextField()
    guests = models.ManyToManyField(Guest, related_name="events")
    
    def __str__(self) -> str:
        return self.title
    
