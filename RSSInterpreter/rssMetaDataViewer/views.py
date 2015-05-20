from django.shortcuts import render

from .models import RssVideo

def index(request):
	testVideo = { 'codec': "video/mp4", 'duration': 185, 'bitrate': 128 }
	context = RequestContext(request, {
		'videos': [testVideo]
	})
	return render(request, 'rssMetaDataViewer/index.html', context))

