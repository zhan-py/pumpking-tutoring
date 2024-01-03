from django.urls import path
from .views import dashboard, view_booking, profile

urlpatterns = [
  path('', dashboard, name='dashboard'),
  path('profile/', profile, name='profile'),
  path('view_booking/<int:booking_id>/', view_booking, name='view_booking'),
]