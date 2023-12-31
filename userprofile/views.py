from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from booking.models import Booking
from userprofile.models import ConversationMessage
from notification.utilities import create_notification
from notification.models import Notification


@login_required
def dashboard(request):
  return render(request, 'userprofile/dashboard.html', {'userprofile': request.user.userprofile})


@login_required
def view_booking(request, booking_id):
  if request.user.userprofile.is_tutor:
    booking = get_object_or_404(Booking, pk=booking_id, tutor=request.user)
    if request.method == 'POST':
      content = request.POST.get('content')
      if content:
        conversationMessage = ConversationMessage.objects.create(booking=booking, content=content, created_by=request.user)
        create_notification(request, booking.tutee, notification_type=Notification.MESSAGE, booking_id = booking.id)
        return redirect('view_booking', booking_id)
  else:
    booking = get_object_or_404(Booking, pk=booking_id, tutee=request.user)
    if request.method == 'POST':
      content = request.POST.get('content')
      if content:
        conversationMessage = ConversationMessage.objects.create(booking=booking, content=content, created_by=request.user)
        create_notification(request, booking.tutor, notification_type=Notification.MESSAGE, booking_id = booking.id)
        return redirect('view_booking', booking_id)
  return render(request, 'userprofile/view_booking.html', {'booking': booking})