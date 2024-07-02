from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import os

class CustomUser(AbstractUser):
    def image_upload_to(self, filename):
        # Construct the upload path based on user email and filename
        return os.path.join("Users", self.email, filename)

    STATUS_CHOICES = (
        ('regular', 'Regular'),
        ('subscriber', 'Subscriber'),
        ('moderator', 'Moderator'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='regular')
    description = models.TextField("Description", max_length=600, default='', blank=True)
    image = models.ImageField(default='default/user.jpg', upload_to=image_upload_to, blank=True)

    def __str__(self):
        return self.username

from django.db import models
from django.utils import timezone

class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email
