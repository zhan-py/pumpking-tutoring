from django.urls import path
from .views import dashboard, view_booking

urlpatterns = [
  path('', dashboard, name='dashboard'),
  path('view_booking/<int:booking_id>/', view_booking, name='view_booking'),
]