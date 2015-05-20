from django.db import models

# Manager class for creating/controlling RssVideoManager models
class RssVideoManager(models.Manager):
    def createRssVideo(self, codec, duration, bitrate):
        rssVideo = self.create(codec=codec, duration=duration, bitrate=bitrate)
        return rssVideo

# Model for storing video meta data from an RSS feed
class RssVideo(models.Model):

	# Codec of video (MIME type) contained in RSS feed (Ex: "video/mp4")
	# If the codec is not in media:content, media:player must be defined
    codec = models.CharField(max_length=32)

    # Length of movie clip in seconds (Ex: "225")
    duration = models.IntegerField()

    # Data rate of movie clip in kb/s (Ex: "128")
    bitrate = models.IntegerField()

    # Bind this model to its manager
    objects = RssVideoManager()
