from django.test import SimpleTestCase
from django.core.urlresolvers import reverse

from utility.rssHelpers import feedparserWrapper
from .models import RssVideo

class RssMetaDataViewerViewTests(SimpleTestCase):

    def test_index_noVideoMetaData_EmptyPageWithMessage(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Found")

class RssHelpersTests(SimpleTestCase):

    def setUp(self):
        self.testEntry = {'title': 'Some Title',
        'media_credit': [{ 'content': 'Red Bull' }],
        'media_content': [{
            'url': u'http://www.img.com/movie.mp4',
            'type': 'video/mp4',
            'duration': "60",
            'filesize': "61440" # <-- 1 KB/s because 6144 B * (1 KB / 1024 B) / 60 s = 1
        }],
        'media_thumbnail': [
          {'url': u'http://www.img.com/img1.jpg', 'width': u'480', 'height': u'360'},
          {'url': u'http://www.img.com/img1_small.jpg', 'width': u'180', 'height': u'136'},
          {'url': u'http://www.img.com/img1_tiny.jpg', 'width': u'80', 'height': u'60'},
          {'url': u'http://www.img.com/img1_max.jpg', 'width': u'560', 'height': u'480'}
        ]}

    def test_createVideoDictsFromEntry_validMetaData_returnValidDict(self):
        """
        createRssDictFromEntry should parse the media_content dict, retrieve the type, duration and fileSize
        then use those strings to create the codec string, duration int and bitrate int
        """
        parser = feedparserWrapper()
        videoDicts = parser.createVideoDictsFromEntry(self.testEntry)
        self.assertEqual(videoDicts[0]['codec'], "mp4")
        self.assertEqual(videoDicts[0]['duration'], 60)
        self.assertEqual(videoDicts[0]['bitrate'], 1)

    def test_getSmallestThumbnailFromEntry_validImages_returnSmallestImgUrl(self):
        """
        getSmallestThumbnailFromEntry should calculate the area of each img and return
        the url of the smallest one
        """
        parser = feedparserWrapper()
        url = parser.getSmallestThumbnailFromEntry(self.testEntry)
        self.assertEqual(url, u'http://www.img.com/img1_tiny.jpg')


class RssVideoModelTests(SimpleTestCase):

    def test_constructor_noCodecPassed_shouldError(self):
        """
        __init__() should raise an exception when given no codec
        """
        exceptionRaised = False
        try:
        	rssVideo = RssVideo()
        except Exception as exception:
        	exceptionRaised = True

        self.assertEqual(exceptionRaised, True)

    def test_constructor_minValuesPassed_shouldNotError(self):
        """
        __init__() should raise an exception when given no codec
        """
        exceptionRaised = False
        try:
            rssVideo = RssVideo(codec="video/mp4")
        except Exception as exception:
            exceptionRaised = True

        self.assertEqual(exceptionRaised, False)

    def test_constructor_validValuesPassed_shouldOverrideDefaults(self):
        rssVideo = RssVideo("video/mp4",200) 
        self.assertEqual(rssVideo.duration, 200)
