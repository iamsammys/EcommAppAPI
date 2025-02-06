from django.db import models
from user.models import User
from shared_model.basemodel import Basemodel


class ProductCategory(Basemodel):
    """
    Model for categories

    Attributes:
        name (str): name of the category
        description (str): description of the category
        image (str): image of the category
    """
    name = models.CharField(max_length=150)
    description = models.TextField()

class Product(Basemodel):
    """
    Model for products

    Attributes:
        name (str): name of the product
        description (str): description of the product
        price (float): price of the product
        quantity (int): quantity of the product
        image (str): image of the product
        user_id (int): id of the user that created the product
    """
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    
class ProductReview(Basemodel):
    """
    Model for product reviews

    Attributes:
        product_id (int): id of the product
        user_id (int): id of the user that created the review
        rating (int): rating of the product
        review (str): review of the product
    """
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

class Wishlist(Basemodel):
    """
    Wishlist model

    Attributes:
        user_id (User): the user that owns the wishlist
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class WishlistItem(Basemodel):
    """
    Model to store user wishlist
    
    Attributes:
        user_id (int): id of the user
        product_id (int): id of the product
    """
    wishlist_id = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)