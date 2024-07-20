from django.db import models

class Event(models.Model):
    event_image = models.ImageField(upload_to='event_images/')
    event_name = models.CharField(max_length=200)
    event_date_from = models.DateField()
    event_date_to = models.DateField()
    event_place = models.CharField(max_length=200)
    event_time_from = models.TimeField()
    event_time_to = models.TimeField()
    event_website_link = models.URLField(blank=True, null=True)  # Optional
    about_event = models.TextField()

    def __str__(self):
        return self.event_name
