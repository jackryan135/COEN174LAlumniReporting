# Generated by Django 2.1.2 on 2018-11-12 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_auto_20181030_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='attended',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance.Event'),
        ),
    ]
