from django.shortcuts import render

from utility.rssHelpers import feedparserWrapper
from .models import RssVideo

def index(request):
	# testVideo = RssVideo(codec="video/mp4", duration=185, bitrate=128)
	parser = feedparserWrapper()
	context = { 'rssData': parser.getRssData() }

	return render(request, 'rssMetaDataViewer/index.html', context)

