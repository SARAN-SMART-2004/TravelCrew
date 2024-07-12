from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("edit_all_travel_plans/", views.edit_all_travel_plans, name="edit_all_travel_plans"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("people/", views.people, name="people"),
    path("upcoming-trips/", views.upcoming_trips, name="upcoming_trips"),
    path("ongoing-trips/", views.ongoing_trips, name="ongoing_trips"),
    path('past-trips/', views.past_trips, name='past_trips'),
    path('submit-travel-plan/', views.submit_travel_plan, name='submit_travel_plan'),
    path('all-travel-plans/', views.all_travel_plans, name='all_travel_plans'),
    path('edit-travel-plan/<int:pk>/', views.edit_travel_plan, name='edit_travel_plan'),
    path('user-post-history/', views.user_post_history, name='user_post_history'),
    path('travel_plan/<int:pk>/', views.travel_plan_details, name='travel_plan_details'),
    
    
    
] 