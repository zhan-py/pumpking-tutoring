from django.db import models
from django.contrib.auth.models import User
from booking.models import Booking
from PIL import Image

class Userprofile(models.Model):
  user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
  is_tutor = models.BooleanField(default=False)
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')
  self_intro = models.TextField(default='')
  brief_intro = models.TextField(default='')
  hourly_rate = models.FloatField(default=0)

  def __str__(self) -> str:
    return self.user.username
  
  def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        width, height = img.size  # Get dimensions

        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 300 and height > 300:
            img.thumbnail((300, 300))

        img.save(self.image.path)
  
  
User.userprofile = property(lambda u: Userprofile.objects.get_or_create(user=u)[0])


class ConversationMessage(models.Model):
  booking = models.ForeignKey(Booking, related_name='conversationmessages', on_delete=models.CASCADE)
  content = models.TextField()
  created_by = models.ForeignKey(User, related_name='conversationmessages', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['created_at']