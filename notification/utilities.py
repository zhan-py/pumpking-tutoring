from .models import Notification

def create_notification(request, to_user, notification_type, booking_id):
  notification = Notification.objects.create(to_user=to_user, notification_type=notification_type, booking_id=booking_id, created_by=request.user)