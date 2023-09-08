from django.db import models
from django.db.models import JSONField

x={"email": "to1@example.com"}

class Event(models.Model):
    title = models.CharField(max_length=30)
    photo = models.ImageField(null=True, blank=True, upload_to="static/uploads/")
    notes = models.TextField(max_length=100)
    location = models.CharField(max_length=30)
    attendees = models.IntegerField(blank=True, null=True)
    names = JSONField("names", default={"john": "john@example.com"})

    def __str__(self):
        return self.title

