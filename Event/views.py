from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
import json

from Event.models import Event

def all_events(request):
	eventList = Event.objects.all()
	return render(request, 'Event/all_events.html', {'eventList': eventList})


def view_event(request, id):
    event = Event.objects.get(id=id)

    username = request.user.username

    attendeeList = event.names


    # if the user has chosen to attend the event, we add their name to the event model
    # and increment the attendees counter. Likewise, we decrement the attendees counter
    # and remove their name from the list if the user has changed their mind
    if 'attending' in request.POST:
        attendeeList["names"].append(username)
        event.attendees += 1
        event.save()
    if 'not_attending' in request.POST:
        
        # removing an item from JSON requires us to know the index, so we must loop
        # through every name until we find the username
        size = len(attendeeList["names"])
        for i in range(size):
            if attendeeList["names"][i] == username:
                attendeeList["names"].pop(i)

        event.attendees -= 1
        event.save()

    # pass true or false so that the template knows weather to render the signup
    # or remove button from the event page
    if username in attendeeList["names"]:
        signedUp = True
    else:
        signedUp = False

    return render(request, 'Event/view_event.html', {'event': event, 'signedUp': signedUp})