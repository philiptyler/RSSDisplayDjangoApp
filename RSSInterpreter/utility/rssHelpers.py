import feedparser

# Helper class to call feedparser functions and generate
# the rss dicts needed to run the page
class feedparserWrapper:

	defaultUrl = 'http://www.wdcdn.net/rss/presentation/library/client/iowa/id/128b053b916ea1f7f20233e8a26bc45d'

	# optional argument to give custom URL
	def __init__(self, **kwargs):
		if 'url' in kwargs:
			self.url = kwargs['url']
		else:
			self.url = self.defaultUrl

	# Parses RSS url, loops through all media content generating video rss dicts
	def getRssData(self):
		rssData = feedparser.parse(self.url)
		rssDataDict = []
		
		for entry in rssData.entries:
			rssDataDict.append({
				'title': entry['title'],
				'videoData': self.createRssDictFromEntry(entry),
				'thumbnailUrl': self.getSmallestThumbnailFromEntry(entry)
			})

		return rssDataDict

	# convert the strings in the content dict to more commom readable entries
	def createRssDictFromEntry(self, entry):
		# entry could be a media:group and have multiple contents in media_content
		rssVideoDataDicts = []
		for content in entry['media_content']:
			slashIndex = content['type'].index('/')+1
			codec = content['type'][slashIndex:]
			duration = int(content['duration'])
			fileSizeKB = float(content['filesize'])/ 1024
			bitrate = int(round(fileSizeKB / duration))
			rssVideoDataDicts.append({'codec': codec, 'duration': duration, 'bitrate': bitrate })

		return rssVideoDataDicts

	def getSmallestThumbnailFromEntry(self, entry):
		smallestThumbnailSize = 0
		smallestThumbnailUrl = ""
		for thumbnail in entry['media_thumbnail']:
			thumbnailSize = int(thumbnail['width']) * int(thumbnail['height'])
			if (smallestThumbnailSize == 0 or smallestThumbnailSize > thumbnailSize):
				smallestThumbnailSize = thumbnailSize
				smallestThumbnailUrl = thumbnail['url']

		return smallestThumbnailUrl
