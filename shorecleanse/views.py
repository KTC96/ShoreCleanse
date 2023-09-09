from django.shortcuts import render
from Event.models import Event

def index(request):
    eventList = Event.objects.all()
    return render(request, 'index.html', {'eventList': eventList})

def about(request):
	return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')