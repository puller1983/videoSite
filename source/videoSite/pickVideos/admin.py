from django.contrib import admin

# Register your models here.

from .models import Parent, Children, VideoUrl

admin.site.register(Parent)
admin.site.register(Children)
admin.site.register(VideoUrl)
