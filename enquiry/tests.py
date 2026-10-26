from django.test import TestCase
from django.urls import reverse
from .models import Enquiry
class PortfolioTests(TestCase):
    def test_home(self):
        response = self.client.get(reverse("enquiry:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "S. Yashwanth")
        self.assertContains(response, "/static/style.css")
    def test_submit(self):
        response = self.client.post(reverse("enquiry:home"), {"name":"Test Visitor", "email":"visitor@example.com", "message":"Project enquiry"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Enquiry.objects.count(), 1)
    def test_invalid_email(self):
        response = self.client.post(reverse("enquiry:home"), {"name":"Visitor", "email":"invalid", "message":"Hello"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Enquiry.objects.count(), 0)
    def test_honeypot(self):
        self.client.post(reverse("enquiry:home"), {"name":"Bot", "email":"bot@example.com", "message":"Hi", "website":"spam"})
        self.assertEqual(Enquiry.objects.count(), 0)
    def test_cooldown(self):
        data = {"name":"Visitor", "email":"visitor@example.com", "message":"Hello"}
        self.client.post(reverse("enquiry:home"), data)
        self.client.post(reverse("enquiry:home"), data)
        self.assertEqual(Enquiry.objects.count(), 1)
