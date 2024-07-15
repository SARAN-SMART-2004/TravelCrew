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
    path('accept_trip/<int:pk>/', views.accept_trip, name='accept_trip'),
    path('travel_plan/<int:pk>/', views.TravelPlanDetailView.as_view(), name='travel_plan_detail'),
    path('people/<int:pk>/', views.user_profile, name='user_profile'),  
    path('search/', views.search_travel_plans, name='search_travel_plans'),
    path('messages/', views.user_messages, name='messages'),
    path('requests/', views.requests, name='requests'),
    


    
    
    
    
    
] 