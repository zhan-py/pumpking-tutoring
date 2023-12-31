from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
  BOOKING = 'booking'
  MESSAGE = 'message' 
  CHOICES = (
    (BOOKING, 'Booking'),
    (MESSAGE, 'Message') 
  )

  notification_type = models.CharField(max_length=20, choices=CHOICES)
  created_by = models.ForeignKey(User, related_name='creatednotifications', on_delete=models.CASCADE)
  to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
  is_read = models.BooleanField(default=False)
  booking_id = models.IntegerField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-created_at']