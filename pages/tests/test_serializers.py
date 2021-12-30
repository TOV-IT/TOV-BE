import json
import unittest
from django.core.exceptions import ValidationError

from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse

from pages.models import *
from pages.utils import construct_component
from pages.serializers import *



class ComponentTest(unittest.TestCase):
    fixture = []
    
    def setUp(self):
        page = Page()
        page.save()
        self.addfixture(page)
        
    def tearDown(self):
        for f in self.fixture:
            f.delete()
    
    def addfixture(self, obj):
        self.fixture.append(obj)
    
    def getPage(self):
        return [p for p in self.fixture if isinstance(p, Page)][0]
    
    
    def test_ComponentCreateSerializer(self):
        print(self.getPage().pk)
        data = {
            "title": "TITLE",
            "sub_title": "sub",
            "body": "test",
            "order": 2,
            "type": 'gallery',
            'sub_type': "gallery2",
            "bg_color_code": "#FFF",
            "page": self.getPage().pk,
            "pageimages": [
                {
                    "alt": "testimage1",
                    "image_url": "https://cloud.com",
                    "order": 5
                },
                {
                    "alt": "testimage2",
                    "image_url": "https://cloud.com",
                    "order": 6
                }
            ]
        }
        
        serializer = ComponentCreateSerializer(data=data)
        if not serializer.is_valid():
            raise ValidationError(serializer._errors)
        component = serializer.save()
        self.addfixture(component)
        
        
if __name__ == '__main__':
    unittest.main()
        