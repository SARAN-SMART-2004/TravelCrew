from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'event_image',
            'event_name',
            'event_date_from',
            'event_date_to',
            'event_place',
            'event_time_from',
            'event_time_to',
            'event_website_link',
            'about_event',
        ]
        widgets = {
            'event_date_from': forms.DateInput(attrs={'type': 'date'}),
            'event_date_to': forms.DateInput(attrs={'type': 'date'}),
            'event_time_from': forms.TimeInput(attrs={'type': 'time'}),
            'event_time_to': forms.TimeInput(attrs={'type': 'time'}),
        }
