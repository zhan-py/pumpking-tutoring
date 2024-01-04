from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from booking.models import Booking
from userprofile.models import ConversationMessage
from notification.utilities import create_notification
from notification.models import Notification
from .forms import UserUpdateForm, ProfileUpdateForm, TuteeProfileUpdateForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage


@login_required
def dashboard(request):
  if request.user.userprofile.is_tutor:
    bookings = request.user.bookings_received.all()
  else:
    bookings = request.user.bookings_made.all()
  
  items_per_page = 10
  paginator = Paginator(bookings, items_per_page)
  page_number = request.GET.get('page', 1)
  try:
    page = paginator.page(page_number)
  except EmptyPage:
    page = paginator.page(paginator.num_pages)

  return render(request, 'userprofile/dashboard.html', {'userprofile': request.user.userprofile, 'page': page})


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


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if request.user.userprofile.is_tutor:
            p_form = ProfileUpdateForm(request.POST,
                                      request.FILES,
                                      instance=request.user.userprofile)
        else:
            p_form = TuteeProfileUpdateForm(request.POST,
                                      request.FILES,
                                      instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        if request.user.userprofile.is_tutor:
            p_form = ProfileUpdateForm(instance=request.user.userprofile)
        else:
            p_form = TuteeProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'userprofile/profile.html', context)