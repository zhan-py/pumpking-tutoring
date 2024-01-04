from django import forms
from .models import Booking, Subject

class AddBookingForm(forms.ModelForm):
  # def __init__(self, *args, **kwargs):
  #   super().__init__(*args, **kwargs)
  #   self.fields['subject'].queryset = self.get_subjects()

  # def get_subjects(self):
  #   tutor = getattr(self.instance, 'tutor', None)
  #   print(self.instance)
  #   if self.instance:
  #     return self.instance.userprofile.program.subjects.all()
  #   return Subject.objects.none()
  def __init__(self, *args, **kwargs):
        tutor_program_subjects = kwargs.pop('tutor_program_subjects', None)
        super(AddBookingForm, self).__init__(*args, **kwargs)

        if tutor_program_subjects:
            self.fields['subject'].queryset = tutor_program_subjects

  class Meta:
    model = Booking
    fields = ['subject', 'date', 'start_time', 'end_time']
    widgets = {
        'date': forms.DateInput(attrs={'type': 'date'}),
        'start_time': forms.TimeInput(attrs={'type': 'time'}),
        'end_time': forms.TimeInput(attrs={'type': 'time'}),
    }
