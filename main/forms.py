# forms.py

from django import forms
from .models import TravelPlan

class TravelPlanForm(forms.ModelForm):
    class Meta:
        model = TravelPlan
        fields = ['source_place', 'destination_place', 'date', 'leaving_time', 'waiting_time', 'message', 'organizer']
