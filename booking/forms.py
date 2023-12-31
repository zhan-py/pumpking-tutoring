from django import forms
from .models import Booking

class AddBookingForm(forms.ModelForm):
  class Meta:
    model = Booking
    fields = ['subject', 'date', 'start_time', 'end_time']