from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import RssVideo

def index(request):
	testVideo = { 'codec': "video/mp4", 'duration': 185, 'bitrate': 128 }
	template = loader.get_template('rssMetaDataViewer/index.html')
	context = RequestContext(request, {
		'videos': [testVideo]
	})
	videos = [testVideo]
	return HttpResponse(template.render(context))

