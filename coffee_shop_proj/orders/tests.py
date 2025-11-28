from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class MyOrderViewTests(TestCase):
    def test_no_logged_user_should_redirect_to_login(self):
        url = reverse("my_order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        redirect_url = reverse("login") + f"?next={url}"
        self.assertEqual(response.url, redirect_url)

    def test_logged_user_should_return_302(self):
        User = get_user_model()
        user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username=user.username, password=user.password)

        url = reverse("my_order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
