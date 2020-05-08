from django.test import TestCase
from api.models import User

class AnimalTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="lion", traits="roar")
        User.objects.create(name="cat", traits="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = User.objects.get(name="lion")
        cat = User.objects.get(name="cat")
        self.assertEqual(lion.name, 'lion')
        self.assertEqual(cat.name, 'cat')