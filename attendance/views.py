from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from attendance.models import Event
from .forms import SignUpForm, EventForm
from datetime import datetime


today = datetime.today()
now = datetime.now()


# Create your views here.
def index(request):
    num_future_events = Event.objects.filter(date__gte=today).count()
    query_set = Event.objects.filter(date__gte=today).order_by('date', 'time')[:3]

    context = {
        'num_future_events': num_future_events,
        'query_set': query_set
    }

    return render(request, 'index.html', context=context)


class EventListView(generic.ListView):
    model = Event
    query_set = Event.objects.filter(date__gte=today).order_by('date', 'time')[:21]
    template_name = 'listPage.html'


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'eventDetail.html'


def RegisterUser(request):
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


def CreateEvent(request):
    event_form = EventForm(data=request.POST)
    if event_form.is_valid():
        event = event_form.save()
        return redirect('event_detail', pk=event.pk)
    else:
        event_form = EventForm()
    return render(request, "eventForm.html", {'form': event_form})
