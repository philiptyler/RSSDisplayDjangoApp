from django.test import SimpleTestCase
from django.core.urlresolvers import reverse

from .models import RssVideo

class RssMetaDataViewerViewTests(SimpleTestCase):

    def test_index_noVideoMetaData_EmptyPageWithMessage(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Found")

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
