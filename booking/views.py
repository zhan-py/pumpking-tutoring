from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import AddBookingForm
from notification.utilities import create_notification
from notification.models import Notification

@login_required
def make_booking(request, tutor_id):
  tutor = User.objects.get(pk=tutor_id)
  if request.method == 'POST':
    form = AddBookingForm(request.POST)
    if form.is_valid:
      booking = form.save(commit=False)
      booking.tutee = request.user
      booking.tutor = tutor
      booking.save()
      create_notification(request, to_user = tutor, notification_type=Notification.BOOKING, booking_id = booking.id)

      return redirect('dashboard')
  else:
    form = AddBookingForm()

  return render(request, 'booking/make_booking.html', {'form': form})   
