from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.views import generic
from attendance.models import Event
from .forms import SignUpForm, EventForm, AttendForm
from datetime import datetime


today = datetime.today()
now = datetime.now()


# Create your views here.
def index(request):
    num_future_events = Event.objects.filter(date__gte=today).filter(approved=True).count()
    query_set = Event.objects.filter(date__gte=today).filter(approved=True).order_by('date', 'time')[:3]

    context = {
        'num_future_events': num_future_events,
        'query_set': query_set
    }

    return render(request, 'index.html', context=context)


class EventListView(generic.ListView):
    model = Event
    query_set = Event.objects.filter(date__gte=today).exclude(approved=False).order_by('date', 'time')[:21]
    template_name = 'listPage.html'

    def get_queryset(self):
        return self.query_set.all()  # all forces the query set to update


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


def reports(request):
    event_list = Event.objects.all()
    event_list = event_list.filter(approved=True, date__lte=today)
    event_list = event_list.order_by('-date', 'time')
    paginator = Paginator(event_list, 10)  # Show 10 contacts per page

    page = request.GET.get('page')
    events = paginator.get_page(page)
    return render(request, 'reportPage.html', {'events': events})


def attendanceList(request, pk):
    event = Event.objects.get(pk=pk)
    alumni = event.alumni_set.all()
    return render(request, 'attendList.html', {'alumni': alumni})
