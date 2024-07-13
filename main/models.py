from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

class TravelPlan(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_travel_plans')
    source_place = models.CharField(max_length=255)
    destination_place = models.CharField(max_length=255)
    date = models.DateField()
    leaving_time = models.TimeField()
    message = models.TextField(blank=True)
    waiting_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name='accepted_travel_plans')


    def __str__(self):
        return f"{self.source_place} to {self.destination_place} on {self.date}"
    

class JoinRequest(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    travel_plan = models.ForeignKey(TravelPlan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} -> {self.travel_plan}"

    


    
