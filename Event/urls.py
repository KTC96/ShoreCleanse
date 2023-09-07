from django.urls import path

from . import views

urlpatterns = [
    path('view_event/<id>', views.view_event, name='view_event'),
    path('all_events', views.all_events, name='all_events'),
]