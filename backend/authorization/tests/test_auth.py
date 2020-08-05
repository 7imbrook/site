from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestLookasideAuth(TestCase):
    def testLoggedOutUser(self):
        client = Client()
        res = client.get("/api/auth/status/")
        self.assertEqual(
            res.status_code, 403, "Status should have failed for logged out user."
        )

    def testLoggedInUser(self):

        user = User.objects.create_superuser(
            username="michael", email="test@example.com", password="123"
        )
        client = Client()
        client.login(username=user.username, password="123")

        res = client.get("/api/auth/status/")
        self.assertEqual(
            res.status_code, 200, "Super user was unable to pass auth test"
        )

