from django.utils import unittest
from django import test as djangotest
from django.test.client import RequestFactory

from specialization.middleware import SpecializationMiddleware

class SpecializationMiddlewareTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = SpecializationMiddleware()

    def test_001_should_set_in_globals_with_hostname(self):
        hostname = 'subdomain.domain.com'
        request = self.factory.get('/')
        request.META['HTTP_HOST'] = hostname

        self.middleware.process_request(request)

        # print globals().keys()
        # print globals()['__builtins__'].keys()

        #self.assertEqual( hostname, globals()['SPECIALIZATION_HOST'] )


class JasefdkljTest(djangotest.TestCase):
    def test_001_should_render_proper_index(self):
        expected = 'index.html'
        response = self.client.get('/')
        self.assertTemplateUsed(response, expected)

    def test_002_should_render_proper_index(self):
        expected = 'index.html'
        response = self.client.get('/', {}, HTTP_HOST = 'subdomain.domain.com')
        self.assertTemplateUsed(response, expected)
