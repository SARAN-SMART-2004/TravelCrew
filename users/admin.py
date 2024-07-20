from django.contrib import admin
from .models import CustomUser,OTP,Feedback,LocalGuides

class SubscribedUsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')

admin.site.register(CustomUser)

admin.site.register(OTP)

admin.site.register(Feedback)

admin.site.register(LocalGuides)