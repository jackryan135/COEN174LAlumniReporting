# Authors: Sam Burns, Simran Judge, Jack Ryan
# views.py: Code that provides the actions that each view takes on the data and specifies the data to show. Connects the templates to a view.
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views import generic
from attendance.models import Event, Alumni
from .forms import EventForm, AttendForm, UpdateForm
from datetime import datetime

# sets the date and time to filter events
today = datetime.today()
now = datetime.now()


# Function Name: index
# Parameters: request
# Description: Gathers the 3 upcoming events to display on the home page. Renders the index template.
def index(request):
    num_future_events = Event.objects.filter(
        date__gte=today).filter(approved=True).count()
    query_set = Event.objects.filter(date__gte=today).filter(
        approved=True).order_by('date', 'time')[:3]

    context = {
        'num_future_events': num_future_events,
        'query_set': query_set
    }

    return render(request, 'index.html', context=context)


# Class Name: EventListView
# Parameters: generic class ListView
# Description: Extends the ListView generic class. Gathers list of events from the database to display, ordered by date and time. Renders the listPage template.
class EventListView(generic.ListView):
    model = Event
    query_set = Event.objects.filter(date__gte=today).exclude(
        approved=False).order_by('date', 'time')[:21]
    template_name = 'listPage.html'

    # Function Description: Overrides the get_queryset() function. Gives the list of upcoming events ordered by date and time.
    def get_queryset(self):
        return self.query_set.all()  # all forces the query set to update


# Class Name: EventDetailView
# Parameters: generic class DetailView
# Description: Extends the DetailView generic class. Displays the name, description, date, time, and location of event. Renders the eventDetail template.
class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'eventDetail.html'


# Class Name: EventUpdateView
# Parameters: generic class UpdateView
# Description: Extends the UpdateView generic class. Verifies and populates the event form for updating. Renders the editEvent template.
class EventUpdateView(generic.UpdateView):
    model = Event
    form_class = UpdateForm
    template_name = 'editEvent.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'event'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.save()
        return redirect('event_detail', pk=event.pk)


"""def RegisterUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})
"""


# Function Name: CreateEvent
# Parameters: request
# Description: Submits the event creation form. Sets value of "approved" variable based on user class. Renders the eventForm template.
def CreateEvent(request):
    event_form = EventForm(data=request.POST)
    if event_form.is_valid():
        event = event_form.save()
        if request.user.is_superuser:
            event.approved = True
            event.save()
        else:
            event.approved = False
            event.save()
        return redirect('event_detail', pk=event.pk)
    else:
        event_form = EventForm()
    return render(request, "eventForm.html", {'form': event_form})


# Function Name: attend
# Parameters: request, pk
# Description: Gathers data from the attendance form and saves it to the database. Increments "numAttended" variable. Renders the attendForm template.
def attend(request, pk):
    alumni_form = AttendForm(data=request.POST)
    if alumni_form.is_valid():
        event = Event.objects.get(pk=pk)
        event.numAttend += 1
        alumni = alumni_form.save(commit=False)
        alumni.attended = event
        event.save()
        alumni.save()
        return redirect('event_detail', pk)
    else:
        alumni_form = AttendForm()
    return render(request, "attendForm.html", {'form': alumni_form})


# Function Name: reports
# Parameters: request
# Description: Populates the list of events with attendance data and orders based on date and time. Provides pages for ease of use. Renders the reportPage template.
def reports(request):
    event_list = Event.objects.all()
    event_list = event_list.filter(approved=True, date__lte=today)
    event_list = event_list.order_by('-date', 'time')
    paginator = Paginator(event_list, 10)  # Show 10 events per page

    page = request.GET.get('page')
    events = paginator.get_page(page)
    return render(request, 'reportPage.html', {'events': events})


# Function Name: attendanceList
# Parameters: request, pk
# Description: Populates a list of all alumni in attendance at an event. Renders the attendList template.
def attendanceList(request, pk):
    event = Event.objects.get(pk=pk)
    alumni = event.alumni_set.all()
    return render(request, 'attendList.html', {'alumni': alumni})


# Function Name: deleteAlumni
# Parameters: request, pk
# Description: Deletes the selected alumni from the database. Decrements the "numAttended" variable. Renders the deleteAlumni template.
def deleteAlumni(request, pk):
    alumni = Alumni.objects.get(pk=pk)
    event = alumni.attended
    event.numAttend -= 1
    alumni.delete()
    event.save()
    return render(request, 'deleteAlumni.html', {'alumni': alumni})


# Function Name: approveEvents
# Parameters: request
# Description: Lists all unapproved events. Provides pages for ease of use. Renders the approveEvents template.
def approveEvents(request):
    event_list = Event.objects.all()
    event_list = event_list.filter(approved=False)
    event_list = event_list.order_by('-date', 'time')
    paginator = Paginator(event_list, 10)  # Show 10 events per page

    page = request.GET.get('page')
    events = paginator.get_page(page)
    return render(request, 'approveEvents.html', {'events': events})


# Function Name: eventSubmittedBy
# Parameters: request, pk
# Description: Gives data on the person who submitted an event for review. Renders the eventSubmittedBy template.
def eventSubmittedBy(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'eventSubmittedBy.html', {'event': event})


# Function Name: eventApproved
# Parameters: request, pk
# Description: Sets the "approved" variable to true for the given event. Renders the eventApproved template.
def eventApproved(request, pk):
    event = Event.objects.get(pk=pk)
    event.approved = True
    event.save()
    return render(request, 'eventApproved.html', {'event': event})


# Function Name: eventDenied
# Parameters: request, pk
# Description: Sets the "approved" variable to false for the given event. Renders the eventDenied template.
def eventDenied(request, pk):
    event = Event.objects.get(pk=pk)
    event.delete()
    return render(request, 'eventDenied.html', {'event': event})


# Function Name: deleteEvent
# Parameters: request, pk
# Description: Deletes the given event from the database. Renders the deleteEvent template.
def deleteEvent(request, pk):
    event = Event.objects.get(pk=pk)
    event.delete()
    return render(request, 'deleteEvent.html', {'event': event})
