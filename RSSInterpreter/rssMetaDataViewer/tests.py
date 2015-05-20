from django.test import SimpleTestCase

from .models import RssVideo

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
        rssVideo = RssVideo(codec="video/mp4", duration=200) 
        self.assertEqual(rssVideo.duration, 200)
