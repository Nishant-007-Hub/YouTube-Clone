from rest_framework import fields, serializers
from .models import showVideos, Comment

class showVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = showVideos
        fields = ('video_id', 'videos', 'thumbnail', 'title', 'description', 'channel_name', 'likes', 'dislikes', 'channel_logo', 'views', 'posted')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_id', 'comment_count', 'main_comment', 'user', 'parent_comment', 'parent_video', 'timestamp')