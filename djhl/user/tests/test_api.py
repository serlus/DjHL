from django.shortcuts import resolve_url as r
from pytest_django.asserts import TestCase
from rest_framework.test import APIClient

from djhl.user.models import User


class UserApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.resp = r("/api/v1/users/")
        self.data = {'name': 'Fulano de Tal',
                     'email': 'fulaho@djhl.com.br'}

    def test_get(self):
        """GET /api/v1/users must return status code 200"""
        resp = self.client.get(self.resp)
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        """POST /api/v1/users with the correct data should return 201"""
        resp = self.client.post(self.resp, self.data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'Fulano de Tal')

    def test_bad_request(self):
        """Must return status_code = 400 when email is invalid"""
        self.data['email'] = 'fulano'
        self.assertEqual(self.client.post(self.resp, self.data).status_code, 400)
