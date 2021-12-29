import json
import unittest

from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse

from pages.models import *
from pages.utils import construct_component
from pages.serializers import *



class ComponentTest(unittest.TestCase):
    def setUp(self):
        page = Page()
        page.save()
        
    def test_ComponentCreateSerializer(self):
        data = {
            "title": "TITLE",
            "sub_title": "sub",
            "body": "test",
            "order": 2,
            "type": 'gallery',
            'sub_type': "gallery2",
            "bg_color_code": "#FFF",
            'page_id': 1,
            'pageimages': [
                {
                    "alt": "testimage1",
                    "image_url": "https://cloud",
                    "order": 5
                },
                {
                    "alt": "testimage2",
                    "image_url": "https://cloud",
                    "order": 6
                }
            ]
        }
        
        serializer = ComponentCreateSerializer(data=data)
        serializer.is_valid()
        print(serializer.validated_data)
        # self.assertEqual(serializer.validated_data, data)
        serializer.save()
        
        
        
        