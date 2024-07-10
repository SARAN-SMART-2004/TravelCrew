from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("editpost/", views.editpost, name="editpost"),
    path("edit/", views.edit, name="edit"),
    path("createpost/", views.createpost, name="createpost"),
    path("poststatus/", views.poststatus, name="poststatus"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("people/", views.people, name="people"),
    
    
    
]