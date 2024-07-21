from django.db import models
from django.conf import settings

class Room(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return f"Room: {self.name} | Id: {self.slug}"
    
class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='chat_images/', blank=True, null=True)
    location = models.JSONField(blank=True, null=True)  # Stores latitude and longitude
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message: {self.content}"
