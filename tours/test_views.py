from unittest import TestCase
from tours.models import Destination
from django.test.client import RequestFactory


class TestIndexDestinationView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_cari_destinasi(self):
        request = self.factory.get('/destination/?cari_destinasi=Pant')
        result = cari
        self.assertEqual(request.cari_destinasi(), '')
        self.fail()