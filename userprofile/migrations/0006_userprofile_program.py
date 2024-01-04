# Generated by Django 5.0 on 2024-01-03 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_subject_program'),
        ('userprofile', '0005_userprofile_brief_intro_userprofile_hourly_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='userprofile', to='booking.program'),
        ),
    ]