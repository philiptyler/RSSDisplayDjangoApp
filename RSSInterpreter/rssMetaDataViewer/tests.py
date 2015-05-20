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
