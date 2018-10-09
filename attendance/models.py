from django.db import models

# Create your models here.


class Event(models.Model):
    """Model representing an Event."""
    name = models.CharField(max_length=200, help_text='Enter an event name')
    description = models.TextField(max_length=1500, help_text='Enter an event description')
    date = models.DateField()
    numAttend = models.IntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.name
