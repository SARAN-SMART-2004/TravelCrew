from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
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
    path('search/',views.search,name="search"),
    path('travel_plan/<int:pk>/', views.travel_plan_details, name='travel_plan_details'),
    path('travel_plan/<str:pk>/', views.travel_plan_details, name='travel_plan_details'),
    path('accept_trip/<int:pk>/', views.accept_trip, name='accept_trip'),
    path('travel_plan/<int:pk>/', views.TravelPlanDetailView.as_view(), name='travel_plan_detail'),
    path('people/<int:pk>/', views.user_profile, name='user_profile'),  
    path('search/', views.search_travel_plans, name='search_travel_plans'),
    path('messages/', views.user_messages, name='messages'),
    path('requests/', views.requests, name='requests'),
    path('my-past-history/', views.user_past_history, name='user_past_history'),
    path('my-upcoming-history/', views.user_upcoming_history, name='user_upcoming_history'),
    path('my-ongoing-history/', views.user_ongoing_history, name='user_ongoing_history'),
    path('filter/', views.filter_travel_plans, name='filter_travel_plans'),
    path('people-histroy/<str:username>/', views.user_travel_history, name='user_travel_history'),
      
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)