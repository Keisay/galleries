import os
from django.shortcuts import render
from django.conf import settings
from django.templatetags.static import static

# Create your views here.
def index(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + "/imgs")
    context = {"imgs": img_list}
    return render(request, "gallery/index.html", context)