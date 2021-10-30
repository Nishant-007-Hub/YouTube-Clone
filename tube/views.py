import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Comment, showVideos
from random import shuffle
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import AnonymousUser, User
from django.contrib import messages
from datetime import datetime
from rest_framework import serializers, viewsets
from .serializers import showVideosSerializer, CommentSerializer


class showVideoViewset(viewsets.ModelViewSet):
    queryset = showVideos.objects.all()
    serializer_class = showVideosSerializer

class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def home(request):
    objs = showVideos.objects.all()
    objs_list = list(objs)
    shuffle(objs_list)
    return render(request, "home.html", {"objs":objs_list})

def watch(request, myid):
    watch_video = showVideos.objects.get(video_id=myid)
    print("ko")
    if request.method == "POST" and "dislikeval" in request.POST:
        watch_video.dislikes += 1
    if request.method == "POST" and "likeval" in request.POST:
        watch_video.likes += 1
    if request.method == "POST" and "subscribebtn" in request.POST:
        watch_video.subscribers += 1
        # likeval = request.POST.get("likeval")
        # print("2ko")
        # print(likeval, "likeval")
        # subscribe = request.POST.get("subscribebtn")
        # print(subscribe, "sub")
        # # watch_video = showVideos.objects.get(video_id=myid)
        # if likeval == "0":
        #     watch_video.likes += 1
        # else:
        #     watch_video.likes -= 1
        # # watch_video.subscribers += 1
        # watch_video.save()
    # if request.method == "POST":
    #     subscribe = request.POST.get("subscribe")
    #     print(subscribe, "sub")

    comments = Comment.objects.filter(parent_video=watch_video)
    # print(watch_video.views, "views")
    allcomments = Comment.objects.all()
    watch_video.views += 1
    watch_video.save()
    allvideo = showVideos.objects.exclude(video_id = myid)
    allvideo_list = list(allvideo)
    shuffle(allvideo_list)
    return render(request, "watch.html", {"watch_video":watch_video, "allvideo":allvideo_list, "comments":comments, "allcomments":allcomments})


def channel(request, c_name):
    channel = showVideos.objects.filter(channel_name=c_name)
    return render(request, "channel.html", {"channel":channel, "c_name":c_name})


def subscribe(request):
    videoid = request.GET.get("videoid")
    print(videoid, "videoid")
    watch_video = showVideos.objects.get(video_id=videoid)

def search(request):
    print("lop")
    query = request.GET.get("query").lower()
    print(query, "query")
    titles = showVideos.objects.filter(title__icontains = query)
    # channel_name = showVideos.objects.filter(channel_name__icontains = "query")
    allresults = titles
    # if more than one filters u can use .union to merge all
    # if allresults.count() == 0:
    #     return HttpResponse("no results")
    return render(request, "search_results.html", {"allresults":allresults, "query":query})

def signup(request):
    print("jiok")
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]


        # Error check
        if password != repassword:
            messages.error(request, "Passwors does not match plz try again")
            # print("here i am")
            return redirect('/')

        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Welcome!! Your account has been successfully created")
            return redirect('/')

    else:
        return HttpResponse("404 not found")



def signin(request):
    if request.method == "POST":
        username = request.POST["loginusername"]
        password = request.POST["loginpass"]

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid credentials, plz try again")
            return redirect("/")
        else:
            login(request, user)
            messages.success(request, "Welcome!! Logged in success")
            # return redirect("/")
            '''below line is for return on same page'''
            return redirect(request.META['HTTP_REFERER'])

def Logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    # return redirect("/")
    return redirect(request.META['HTTP_REFERER'])


def postComment(request):
    # print("top")
    if request.method == "POST":
        # commentid = request.POST.get("commentid")
        comment_des = request.POST.get("commentdes")
        reply = request.POST.get("replybox")
        parentvideo_id = request.POST.get("parentvideo_id") 
        # parentvideo_channel = request.POST.get("parentvideo_channel") 
        parent_video =  showVideos.objects.get(video_id=parentvideo_id) 
        print(parent_video, "paren")
        add_comment = Comment(main_comment=comment_des, parent_video=parent_video)
        # add_comment.comment_count = Comment.comment_count + 1
        add_comment.comment_count += 1
        # print(request.user, "jio")
        # if request.user.is_authenticated :
        add_comment.user = request.user
        # add_comment.parent_video = showVideos.objects.get(video_id=parentvideo_id)
        # dic = {"a":a}
        # for i in dic:
        #     add_comment.parent_video = i
        add_comment.timestamp = datetime.now()
        print("1")
        if not reply:
            add_comment.save()
            print(add_comment.comment_id, "main comt id")
        else:
            print("jio")
            comment_des = request.POST.get("replybox")
            parentSno = request.POST.get("parentSno")
            parentcomment = Comment.objects.get(comment_id=parentSno)
            print(parentcomment.comment_id, "reply parecom id")
            add_comment = Comment(main_comment=comment_des, parent_video=parent_video, parent_comment=parentcomment, user=request.user, timestamp=datetime.now())
            add_comment.save()
            print(add_comment.parent_comment.comment_id, "addcoparid")
            print(add_comment.comment_id, "reply main id")

        messages.success(request, "U just comment...")
        # return redirect("/")
        return redirect(request.META['HTTP_REFERER'])

    else:
        return HttpResponse("404 not found")

