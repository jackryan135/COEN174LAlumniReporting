from django.db import models

# Create your models here.

class Alumni(models.Model):
    fName = models.CharField(max_length=45, help_text='Enter your first name')
    lName = models.CharField(max_length=45, help_text='Enter your last name')
    email = models.EmailField()
    school = models.CharField(max_length=50, help_text='Enter school graduated from')
    yearGrad = models.PositiveSmallIntegerField(help_text='Enter graduation year')
    major = models.CharField(max_length=70, help_text='Enter your major')

    def __str__(self):
        return self.fname + ' ' + self.lname


class Event(models.Model):
    """Model representing an Event."""
    name = models.CharField(max_length=200, help_text='Enter an event name')
    description = models.TextField(max_length=1500, help_text='Enter an event description')
    location = models.CharField(max_length=75, help_text='Enter location of event')
    date = models.DateField()
    time = models.TimeField()
    numAttend = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    createdBy = Alumni()

    def __str__(self):
        """String for representing the Model object."""
        return self.name
