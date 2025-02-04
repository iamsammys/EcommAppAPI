from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from shared_model.basemodel import Basemodel

class CustommUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model
    """

    def create_user(self, username: str, password=None, **extra_fields):
        """Create and return a regular user with an email and password
        
        args:
            username: str, required
            password: str, optional
        """
        if username is None:
            raise TypeError("Enter a username.")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username: str, password=None, **extra_fields):
        """Create and return a superuser with an email and password
        
        args:
            username: str, required
            password: str, required
        """
        if password is None:
            raise TypeError("Superusers must have a password.")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
                
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin, Basemodel):
    """Extends the default User model to include additional fields"""

    username = models.CharField(max_length=150, unique=True)
    USERNAME_FIELD = 'username'
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustommUserManager()


class UserProfile(Basemodel):
    """Model for user profile
    
    Attributes: 
        user: User, required
        first_name: str, required
        last_name: str, required
        email: str, required
        phone_number: str, required
        address: str, required
        date_of_birth: date, required
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, max_length=150)
    last_name = models.CharField(blank=True, max_length=150)
    email = models.EmailField(blank=True, max_length=150)
    phone_number = models.CharField(blank=True, max_length=15)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)