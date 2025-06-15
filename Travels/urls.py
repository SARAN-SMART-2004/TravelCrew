from django.urls import path
from . import views

urlpatterns = [
    path('my-travels/', views.travel_list, name='travel_list'),
    path('travel/create/', views.travel_create, name='travel_create'),
    path('travel/<int:pk>/', views.travel_detail, name='travel_detail'),
    path('travel/<int:pk>/edit/', views.travel_edit, name='travel_edit'),
    path('travel/<int:pk>/mark-completed/', views.mark_travel_completed, name='mark_travel_completed'),
    path('completed-travels/', views.completed_travel_list, name='completed_travel_list'),
    path('travel/<int:pk>/upload-memories/', views.upload_memories, name='upload_memories'),
    path('travel/<int:pk>/show-memories/', views.show_memories, name='show_memories'),
]
