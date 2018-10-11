from django.shortcuts import render
from django.views import generic
from attendance.models import Event
from datetime import datetime


today = datetime.today()
now = datetime.now()


# Create your views here.
def index(request):
    num_future_events = Event.objects.filter(date__gte=today).count()
    query_set = Event.objects.filter(date__gte=today, time__gte=now).order_by('date', 'time')[:3]

    context = {
        'num_future_events': num_future_events,
        'query_set': query_set
    }

    return render(request, 'index.html', context=context)


class EventListView(generic.ListView):
    model = Event
    query_set = Event.objects.filter(date__gte=today, time__gte=now).order_by('date', 'time')[:21]
    template_name = 'listPage.html'


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'eventDetail.html'
