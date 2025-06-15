from django.db import models
from django.conf import settings

class Travel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    additional_notes = models.TextField(blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    travel_route = models.TextField(blank=True, null=True)
    travel_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TravelImage(models.Model):
    travel = models.ForeignKey(Travel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='travel_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MemoryImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    travel = models.ForeignKey(Travel, related_name='memory_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='memory_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
