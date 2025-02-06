import pytest
from user.models import (
    User,
    UserProfile
)

@pytest.mark.django_db
def test_user_profile_exist():
    """
    Tests that the user profile is indeed created
    """
    user = User.objects.create_user(username="test_user", password="")
    assert UserProfile.objects.filter(user=user).exists()