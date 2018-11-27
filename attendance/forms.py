#Authors: Sam Burns, Simran Judge, Jack Ryan
#forms.py: Describes the four forms used to receive data from the user interface: LoginForm, EventForm, AttendForm, and UpdateForm.

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Event, Alumni

#Class: LoginForm
#Parameters: AuthenticationForm
#Description: LoginForm allows users to login with their authenticated username and password.
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


"""class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
"""

#Class: EventForm
#Parameters: ModelForm
#Description: EventForm allows users to enter their name, e-mail, school, graduation year, and major in addition to the  name, description, location, date, and time of an Event.
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'location', 'date', 'time', 'event_fName', 'event_lName', 'event_email', 'event_school', 'event_yearGrad', 'event_major', ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }
        labels = {
            'event_fName': "First Name",
            'event_lName': "Last Name",
            'event_email': "E-Mail",
            'event_school': "School",
            'event_yearGrad': "Graduation Year",
            'event_major': "Major",
        }

#Class: AttendForm
#Parameters: ModelForm
#Description: AttendForm allows a user to record attendance by entering the attendee's name, e-mail, school, graduation year, and major.
class AttendForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['fName', 'lName', 'email', 'school', 'yearGrad', 'major', ]
        labels = {
            'fName': "First Name",
            'lName': "Last Name",
            'email': "E-Mail",
            'school': "School",
            'yearGrad': "Graduation Year",
            'major': "Major",
        }

#Class: UpdateForm
#Parameters: ModelForm
#Description: UpdateForm allows a user to update an existing event's name, description, location, date, and time.
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'location', 'date', 'time', ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }
