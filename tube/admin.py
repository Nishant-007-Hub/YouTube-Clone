from django.contrib import admin
from .models import showVideos,Comment

admin.site.register((showVideos,Comment))