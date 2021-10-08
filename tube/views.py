from django.http import HttpResponse
from django.shortcuts import render
from .models import showVideos

def home(request):
    objs = showVideos.objects.all()
    return render(request, "home.html", {"objs":objs})

def watch(request, myid):
    print("asdjf")
    watch_video = showVideos.objects.get(video_id=myid)
    allvideo = showVideos.objects.all()
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
