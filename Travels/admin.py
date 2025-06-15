from django.contrib import admin
from .models import Travel, TravelImage, MemoryImage

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'city', 'state', 'country', 'district', 'travel_completed', 'created_at', 'updated_at')
    list_filter = ('travel_completed', 'created_at', 'updated_at')
    search_fields = ('place_name', 'city', 'state', 'country', 'district')

@admin.register(TravelImage)
class TravelImageAdmin(admin.ModelAdmin):
    list_display = ('travel', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('travel__place_name',)

@admin.register(MemoryImage)
class MemoryImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'travel', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('user__username', 'travel__place_name')
