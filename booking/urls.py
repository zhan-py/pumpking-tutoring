from django.urls import path
from .views import make_booking

urlpatterns = [
  path('make_booking/<int:tutor_id>/', make_booking, name='make_booking'),
]