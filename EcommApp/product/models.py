from django.db import models
from user.models import User
from shared_model.basemodel import Basemodel

class Category(Basemodel):
    """
    Model for categories

    Attributes:
        name (str): name of the category
        description (str): description of the category
        image (str): image of the category
    """
    name = models.CharField(max_length=150)
    description = models.TextField(null=True,
                                   blank=True,
                                   help_text="Enter the category description")
    
    def total_products(self):
        """
        Method to calculate the total number of products in the category
        """
        return self.products.count()

class Product(Basemodel):
    """
    Model for products

    Attributes:
        name (str): name of the product
        description (str): description of the product
        price (float): price of the product
        quantity (int): quantity of the product
        image (str): image of the product
        user (int): id of the user that created the product
    """
    name = models.CharField(max_length=150,
                            help_text="Enter the product name"
                            )
    description = models.TextField(null=True,
                                   blank=True,
                                   help_text="Enter the product description"
                                   )
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                help_text="Enter the product price"
                                )
    quantity = models.PositiveSmallIntegerField(help_text="Enter the product quantity",
                                                validators=[MinValueValidator(1)]
                                                )
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='products'
                             )
    category = models.ForeignKey('ProductCategory',
                                    on_delete=models.CASCADE,
                                    realted_name='products'
                                    )
    
    class Meta:
        ordering = ['created_at']

    def average_rating(self):
        """
        Method to calculate the average rating of the product
        """
        return self.reviews.aggregate(AVG('rating')).get("rating", 0.0)
    
    def total_products(self):
        """
        Method to calculate the total number of products
        """
class Review(Basemodel):
    """
    Model for product reviews

    Attributes:
        product (int): id of the product
        user (int): id of the user that created the review
        rating (int): rating of the product
        review (str): review of the product
    """
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews'
                                )
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, 
                             related_name='reviews'
                             )
    rating = models.IntegerField(choices=RATING_CHOICES,
                                 default=1
                                 )
    review = models.TextField(null=True,
                              blank=True,
                              help_text="Enter the product review"
                              )

class Wishlist(Basemodel):
    """
    Wishlist model

    Attributes:
        user (User): the user that owns the wishlist
    """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='wishlist')

class WishlistItem(Basemodel):
    """
    Model to store user wishlist
    
    Attributes:
        user (int): id of the user
        product (int): id of the product
    """
    wishlist = models.ForeignKey(Wishlist,
                                 on_delete=models.CASCADE,
                                 related_name="items")
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="items")