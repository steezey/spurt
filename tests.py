
from django.test import TestCase, Client
from spurt.models import *

class LinkPostTestCase(TestCase):
    def client_get(self, route):
        Client().get(route)

    def client_post(self, route, params = {}):
        Client().post('/link-posts/create-and-publish/', params)
    
    def test_create_and_publish(self):
        self.client_post(
            '/link-posts/create-and-publish/',
            {
                'uuid': 'test_uuid',
                'url': 'http://www.youtube.com',
                'title': 'test_title',
                'description': 'test_description'
            })
    
    def test_create(self):
        self.client_post(
            '/link-posts/create',
            {
                'uuid': 'test_uuid',
                'url': 'http://www.youtube.com'
            })
