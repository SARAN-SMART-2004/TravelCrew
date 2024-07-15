
from django.contrib import admin
from .models import TravelPlan,TripMessage

@admin.register(TravelPlan)
class TravelPlanAdmin(admin.ModelAdmin):
    list_display = ('source_place', 'destination_place', 'date', 'leaving_time', 'waiting_time', 'organizer', 'created_at')
    search_fields = ('source_place', 'destination_place', 'organizer__username')
    list_filter = ('date', 'organizer')
    ordering = ('-created_at',)

class TripMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'content', 'timestamp')  # Customize the fields to display
    search_fields = ('sender__username', 'recipient__username', 'content')  # Add search functionality

admin.site.register(TripMessage, TripMessageAdmin)
