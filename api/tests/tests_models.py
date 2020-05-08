from django.test import TestCase
from api.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="lion", traits="roar")
        User.objects.create(name="cat", traits="meow")

    def test_adding_users(self):
        """Animals that can speak are correctly identified"""
        lion = User.objects.get(name="lion")
        cat = User.objects.get(name="cat")
        self.assertEqual(lion.traits, 'roar')
        self.assertEqual(cat.traits, 'meow')