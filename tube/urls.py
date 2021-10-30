from django.urls import path
from django.urls.conf import include
from .import views
from rest_framework import routers
from .views import showVideoViewset, CommentViewset

router = routers.DefaultRouter()
router.register(r'showVideos', showVideoViewset)
router.register(r'Comment', CommentViewset)

app_name = "tube"
urlpatterns = [
    path('', views.home, name="home"),
    path('api', include(router.urls)),
    path('watch/<int:myid>', views.watch, name="watch"),
    path('search', views.search, name="search"),
    path('Logout', views.Logout, name="Logout"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('postComment', views.postComment, name="postComment"),
    path('subscribe', views.subscribe, name="subscribe"),
    path('channel/<str:c_name>', views.channel, name="channel"),

]
