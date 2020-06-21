import os
from django.shortcuts import render
from django.conf import settings
from django.templatetags.static import static

# Create your views here.

def home(request):
    return render(request, "gallery/home.html")

def index(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + "/imgs")
    context = {"imgs": img_list}
    return render(request, "gallery/index.html", context)

def index2(request):
    path = settings.MEDIA_ROOT
    vid_list = os.listdir(path + "/vids")
    context = {"vids": vid_list}
    return render(request, "gallery/index2.html", context)

