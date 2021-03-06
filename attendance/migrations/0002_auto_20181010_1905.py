# Generated by Django 2.1.2 on 2018-10-11 02:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.TextField(default=django.utils.timezone.now, help_text='Enter location of event', max_length=75),
            preserve_default=False,
        ),
    ]
