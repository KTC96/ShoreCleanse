from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=30)
    photo = models.ImageField(null=True, blank=True)
    notes = models.TextField(max_length=100)
    location = models.CharField(max_length=30)
    attendees = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

