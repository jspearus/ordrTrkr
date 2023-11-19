from django.db import models
from django.utils import timezone

# Create your models here.
class OrderRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    palets = models.FloatField(max_length=4)
    number_of_cases = models.IntegerField()
    aile_numbers = models.CharField(max_length=60)
    store_number = models.CharField(max_length=2)
    lane_number = models.CharField(max_length=5)
    time_started = models.DateTimeField(default=timezone.now)
    time_finished = models.DateTimeField()
    
    def __str__(self):
        return str(self.store_number) + ' : ' + str(self.id) + ' : ' + str(self.time_started)
    
class StoreTimes(models.Model):
    id = models.BigAutoField(primary_key=True)
    store_number = models.CharField(max_length=2)
    hour_due = models.IntegerField()
    
    def __str__(self):
        return str(self.store_number)