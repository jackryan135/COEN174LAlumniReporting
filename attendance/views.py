from django.shortcuts import render
from attendance.models import Event
from datetime import datetime


# Create your views here.
def index(request):
    today = datetime.today()
    num_future_events = Event.objects.filter(date___gte=today).count()

    context = {
        'num_future_events': num_future_events,
    }

    return render(request, 'index.html', context=context)
