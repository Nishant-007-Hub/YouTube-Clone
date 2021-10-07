from django.db import models
from django.db.models.fields import DateTimeField


class showVideos(models.Model):
    video_id = models.AutoField(primary_key=True)
    videos = models.FileField(upload_to='videos_directory', default="", blank=True)
    thumbnail = models.ImageField(upload_to='Thumbnail', default="")
    title = models.CharField(max_length=50, default="")
    channel_logo = models.ImageField(upload_to="Channel_logo", default="")
    views = models.IntegerField(default=0)
    posted = models.DateTimeField()