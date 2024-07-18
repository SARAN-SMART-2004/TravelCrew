# forms.py

from django import forms
from .models import TravelPlan
from .models import TripMessage,TravelPlan

class TravelPlanForm(forms.ModelForm):
    class Meta:
        model = TravelPlan
        fields = ['source_place', 'destination_place','waiting_place', 'date', 'leaving_time', 'waiting_time', 'message', 'organizer']


class TripMessageForm(forms.ModelForm):
    class Meta:
        model = TripMessage
        fields = ['content', 'recipient']  # Adjust fields as necessary


