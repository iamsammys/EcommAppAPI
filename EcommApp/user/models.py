from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from shared_model.basemodel import Basemodel

class CustommUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model
    """

    def create_user(self, email: str, username, password=None, **extra_fields):
        """Create and return a regular user with an email and password
        
        args:
            username: str, required
            password: str, optional
        """
        if username is None:
            raise TypeError("Enter a username.")
        
        if email is None:
            raise TypeError("Enter an email.")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password=None, **extra_fields):
        """Create and return a superuser with an email and password
        
        args:
            username: str, required
            password: str, required
        """
        if password is None:
            raise TypeError("Superusers must have a password.")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
                
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin, Basemodel):
    """
    Extends the default User model to include additional fields
    
    Attributes:

    """
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
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
        phone_number: str, required
        address: str, required
        date_of_birth: date, required
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank=True, max_length=150)
    last_name = models.CharField(blank=True, max_length=150)
    phone_number = models.CharField(blank=True, max_length=15)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

class Wishlist(models.Model):
    """Model for user wishlist
    
    Attributes:
        user_id: int, required
        product_id: int, required
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE)