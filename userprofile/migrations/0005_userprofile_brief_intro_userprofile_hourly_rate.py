# Generated by Django 5.0 on 2024-01-02 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_userprofile_self_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='brief_intro',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hourly_rate',
            field=models.FloatField(default=0),
        ),
    ]
