from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import camera


class CameraTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_camera = camera.objects.create(name="rake", owner=testuser1, description="Better for collecting leaves than shovel.")
        test_camera.save()

    def test_egg_model(self):
        camera = camera.objects.get(id=1)
        actual_owner = str(camera.owner)
        actual_name = str(camera.name)
        actual_description = str(camera.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(actual_description, "Better for collecting leaves than shovel.")

    def test_empty_description(self):
        # Test if an Camera object can be created without providing a description
        testuser2 = get_user_model().objects.create_user(username='testuser2', password='pass')
        testuser2.save()

        test_camera_no_description = camera.objects.create(name="shovel", owner=testuser2)
        test_camera_no_description.save()

        camera_no_description = camera.objects.get(id=2)
        actual_owner_no_description = str(camera_no_description.owner)
        actual_name_no_description = str(camera_no_description.name)
        actual_description_no_description = str(camera_no_What are the key components and purpose of Django Rest Framework (DRF) permissions, and how do they help in securing an API?

In SQL, what is the purpose of the SELECT statement, and how would you use it to retrieve all columns from a table called ‘employees’?

Can you explain the role of DRF Generic Views and provide examples of their usage in building a RESTful API?description.description)
        self.assertEqual(actual_owner_no_description, "testuser2")
        self.assertEqual(actual_name_no_description, "shovel")
        self.assertEqual(actual_description_no_description, "")  # Empty description should be handled correctly
# Create your tests here.


# Create your tests here.

# Create your tests here.
