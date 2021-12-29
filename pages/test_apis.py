import json
import unittest
from unittest import mock

from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory
from rest_framework import status

from django.contrib.auth.models import User
from django.urls import reverse

from pages.models import *
from pages.utils import construct_component




class ComponentCreateTest(unittest.TestCase):
    client = APIClient()
    headers = {}
    
    def setUp(self):
        user = User.objects.create_superuser(username="admin", email="admin@admin.com", password="admin")
        self.user = user
        
        page = Page()
        page.save()
        
        # user = {
        #     "username": "admin",
        #     "password": "admin"
        # }
        
        # response = self.client.post('', json.dumps(user), content_type='application/json')
        # self.assertEqual(response.status_code, 200, msg="Login Failed")
        
        # self.token = response.data['access_token']
        # self.csrftoken = response.cookies.get('csrftoken').value
        
        # self.assertNotEqual(self.token, '', msg="JWT Token not created")
        
        # self.headers = {
        #     "HTTP_Authorization": "jwt " + self.token,
        #     "X-CSRFToken": self.csrftoken,
        # }
    
    def test_createapi_component(self):
        pass
    
    

