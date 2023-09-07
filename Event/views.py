from django.shortcuts import render, HttpResponseRedirect
from django.views import generic

from Event.models import Event

def all_events(request):
	eventList = Event.objects.all()
	return render(request, 'Event/all_events.html', {'eventList': eventList})


def view_event(request, id):
    event = Event.objects.get(id=id)
    if 'attending' in request.POST:
        event.attendees += 1
        event.save()
    return render(request, 'Event/view_event.html', {'event': event})