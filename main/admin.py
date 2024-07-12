
from django.contrib import admin
from .models import TravelPlan

@admin.register(TravelPlan)
class TravelPlanAdmin(admin.ModelAdmin):
    list_display = ('source_place', 'destination_place', 'date', 'leaving_time', 'waiting_time', 'organizer', 'created_at')
    search_fields = ('source_place', 'destination_place', 'organizer__username')
    list_filter = ('date', 'organizer')
    ordering = ('-created_at',)
