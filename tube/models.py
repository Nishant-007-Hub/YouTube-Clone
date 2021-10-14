from django.db import models
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User
from django.utils.timezone import now


class showVideos(models.Model):
    video_id = models.AutoField(primary_key=True)
    videos = models.FileField(upload_to='videos_directory', default="", blank=True)
    thumbnail = models.ImageField(upload_to='Thumbnail', default="")
    title = models.CharField(max_length=50, default="")
    description = models.TextField(null=True, blank=True)
    subscribers = models.IntegerField(default=0) 
    channel_name = models.CharField(max_length=50, default="")
    channel_logo = models.ImageField(upload_to="Channel_logo", default="")
    views = models.IntegerField(default=0)
    posted = models.DateTimeField()

    def __str__(self):
        return self.title + " " + "|" + " " + self.channel_name

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_count = models.IntegerField(default=0)
    main_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # when u use "self" in ForeignKey it means that section itself a part of that model
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    parent_video = models.ForeignKey(showVideos, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return "comment for" + " " + self.main_comment