from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
import json

from Event.models import Event

def all_events(request):
	eventList = Event.objects.all()
	return render(request, 'Event/all_events.html', {'eventList': eventList})


def view_event(request, id):
    event = Event.objects.get(id=id)

    #if request.user.is_authenticated():
    username = request.user.username

    attendeeList = event.names

    if 'attending' in request.POST:
        attendeeList["names"].append(username)
        event.attendees += 1
        event.save()
    return render(request, 'Event/view_event.html', {'event': event})