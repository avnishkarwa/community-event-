from django.db import models

# Create your models here.


class Events(models.Model):
    events_title = models.CharField(max_length=100)
    events_description = models.TextField()
    events_date = models.DateField()
    events_time = models.TimeField()
    events_organizer_details = models.TextField()
    events_location = models.DecimalField(max_digits=9 , decimal_places=6)
    

 
