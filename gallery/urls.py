from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('waraku', views.index, name='index'),
    path('videos', views.index2, name='index2'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)