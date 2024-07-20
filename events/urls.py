from django.urls import path
from . import views

urlpatterns = [
    path('event-lists/', views.event_list, name='event_list'),
    path('create-event/', views.event_create, name='event_create'),
]
 