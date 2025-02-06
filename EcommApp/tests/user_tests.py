from django.test import TestCase
from user.models import User, UserProfile

class UserSignalTest(TestCase):
    """
    Tests that a user profile is created automatically when a new user is created
    """
    def test_user_profile_exist(self):
        """
        Tests that the user profile is indeed created
        """
        user = User.objects.create_user(username="test_user", password="")
        self.assertTrue(UserProfile.objects.filter(user=user).exists())

    def test_user_must_have_username(self):
        """
        Tests that the user must be created with a username
        """
        with self.assertRaises(TypeError):
            User.objects.create_user(username=None, password="")