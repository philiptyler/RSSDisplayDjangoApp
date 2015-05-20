from django.shortcuts import render

from .models import RssVideo

def index(request):
	testVideo = RssVideo(codec="video/mp4", duration=185, bitrate=128)
	context = { 'videos': [testVideo] }
	return render(request, 'rssMetaDataViewer/index.html', context)

