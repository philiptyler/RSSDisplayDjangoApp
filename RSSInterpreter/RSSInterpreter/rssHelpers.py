import feedparser

class feedparserWrapper:

	defaultUrl = 'http://www.wdcdn.net/rss/presentation/library/client/iowa/id/128b053b916ea1f7f20233e8a26bc45d'

	def __init__(self, **kwargs):
		if 'url' in kwargs:
			self.url = kwargs['url']
		else:
			self.url = self.defaultUrl

	def getRssData(self):
		rssDict = feedparser.parse(self.url)
		
		for entry in rssDict.entries:
			print entry.duration