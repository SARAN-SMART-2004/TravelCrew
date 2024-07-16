from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings

User = get_user_model()  # Get the user model

class TravelPlan(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_travel_plans')
    source_place = models.CharField(max_length=255)
    destination_place = models.CharField(max_length=255)
    waiting_place = models.CharField(max_length=255 ,null=True)
    date = models.DateField()
    leaving_time = models.TimeField()
    waiting_time = models.TimeField()
    message = models.TextField(blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name='accepted_travel_plans')
    

    def __str__(self):
        return f"{self.source_place} to {self.destination_place} on {self.date}"

class JoinRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_plan = models.ForeignKey(TravelPlan, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} -> {self.travel_plan}"


class TripMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()  # Message content
    timestamp = models.DateTimeField(auto_now_add=True)  # When the message was created

    class Meta:
        ordering = ['-timestamp']  # Order messages by timestamp (most recent first)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.recipient.username} at {self.timestamp}'
class Request(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_requests', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_requests', on_delete=models.CASCADE)
    travel_plan = models.ForeignKey(TravelPlan, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Declined', 'Declined')])