from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class TravelPlan(models.Model):
    source_place = models.CharField(max_length=255)
    destination_place = models.CharField(max_length=255)
    date = models.DateField()
    leaving_time = models.TimeField()
    waiting_time = models.TimeField()
    message = models.TextField(blank=True)
    organizer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_place} to {self.destination_place} on {self.date}"
