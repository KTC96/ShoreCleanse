from django.contrib import admin
from django.urls import path, include

from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Event.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('blog/', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('gallery/', views.gallery, name='gallery'),
]
