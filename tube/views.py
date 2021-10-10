import random
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import showVideos
from random import shuffle
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    objs = showVideos.objects.all()
    objs_list = list(objs)
    shuffle(objs_list)
    return render(request, "home.html", {"objs":objs_list})

def watch(request, myid):
    watch_video = showVideos.objects.get(video_id=myid)
    # print(watch_video.views, "views")
    watch_video.views += 1
    watch_video.save()
    allvideo = showVideos.objects.exclude(video_id = myid)
    return render(request, "watch.html", {"watch_video":watch_video, "allvideo":allvideo})

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
            return redirect("/")

def Logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("/")
