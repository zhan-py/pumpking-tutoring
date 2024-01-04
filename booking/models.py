from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Program(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    program = models.ForeignKey(Program, related_name='subjects', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Availability(models.Model):
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  
    start_time = models.TimeField()
    end_time = models.TimeField()


class Booking(models.Model):
    tutee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings_made')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings_received')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
