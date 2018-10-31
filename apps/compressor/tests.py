from django.test import TestCase

from .models import get_random_string


class GetRandomStringTestCase(TestCase):
    def test_string_length(self):
        self.assertEqual(len(get_random_string(5)), 5)

    def test_is_string(self):
        self.assertIsInstance(get_random_string(5), str)

