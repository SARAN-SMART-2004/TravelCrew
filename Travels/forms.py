from django import forms
from .models import Travel, TravelImage

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = [
            'place_name', 'city', 'state', 'country', 'district',
            'additional_notes', 'budget', 'travel_route', 'travel_completed'
        ]
        widgets = {
            'additional_notes': forms.Textarea(attrs={'rows': 4}),
            'travel_route': forms.Textarea(attrs={'rows': 4}),
        }

class TravelImageForm(forms.ModelForm):
    class Meta:
        model = TravelImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }
