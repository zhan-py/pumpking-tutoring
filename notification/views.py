from django.shortcuts import render, redirect
from notification.models import Notification

def notifications(request):
  goto = request.GET.get('goto', '')
  notificaiton_id = request.GET.get('notification')

  if goto != '':
    notification = Notification.objects.get(pk=notificaiton_id)
    notification.is_read = True
    notification.save()
    return redirect('view_booking', booking_id = notification.booking_id)
  
  return render(request, 'notification/notifications.html')
