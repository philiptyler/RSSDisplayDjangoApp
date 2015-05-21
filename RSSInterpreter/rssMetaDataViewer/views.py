from django.shortcuts import render

from utility.rssHelpers import feedparserWrapper
from .models import RssVideo

# single page view for app, takes dict of RSS feed data
# and displays its important data in the index.html template
def index(request):
	parser = feedparserWrapper()
	context = { 'rssData': parser.getRssData() }

	return render(request, 'rssMetaDataViewer/index.html', context)

