from django.shortcuts import render, HttpResponseRedirect
from django.views import generic

from Event.models import Event

def all_events(request):
	eventList = Event.objects.all()
	return render(request, 'Event/all_events.html', {'eventList': eventList})


def view_event(request, id):
    event = event.objects.get(id=id)
    return render(request, 'Event/view_event.html', {'event': event})
