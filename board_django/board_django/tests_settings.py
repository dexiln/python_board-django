import settings
import unittest

class CorrectSettingsTest(unittest.TestCase):

    def test_correct_timezone(self):
        resp = settings.TIME_ZONE
        self.assertEqual(resp, 'UTC')

    def test_correct_language_code(self):
        resp = settings.LANGUAGE_CODE
        self.assertEqual(resp, 'en-us')

    def test_correct_rooturl(self):
        resp = settings.ROOT_URLCONF
        self.assertEqual(resp, 'board_django.urls')