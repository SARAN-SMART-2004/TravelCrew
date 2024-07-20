from django.urls import path
from . import views
from .views import profile, verify_otp
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path("register", views.register, name="register"),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    # path('verify-otp-stored/', views.verify_otp_stored, name='verify_otp_stored'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    path('notes/', views.list_notes, name='list_notes'),
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/delete/<int:note_id>/',  views.delete_note, name='delete_note'),
    path('local-guides/create/', views.local_guides_create, name='local_guides_create'),
    path('local-guides/', views.local_guides_list, name='local_guides_list'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)