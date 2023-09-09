from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

# Register your models here.

@admin.register(Post)
class SomeModelAdmin(SummernoteModelAdmin):
    """
    apply summernote to TextField in model.
    """
    summernote_fields = ('content',)