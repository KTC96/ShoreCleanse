from django.shortcuts import render
from Event.models import Event

def index(request):
    eventList = Event.objects.all()
    total = 0
    weight = 3
    for people in eventList:
         total += people.attendees
    trash_collected = total * weight
    road = trash_collected / 1000
    context = {
         'eventList': eventList,
         'trash_collected': trash_collected,
         'road': road,
         'total': total
    }
    return render(request, 'index.html', context)

def about(request):
	return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')