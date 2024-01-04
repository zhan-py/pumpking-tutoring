from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile


class UserCreationForm(UserCreationForm):
  email = forms.EmailField()

  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password Confirmation'
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['image', 'program', 'hourly_rate', 'brief_intro', 'self_intro']


class TuteeProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['image']