from django.db import models
from django.core.validators import MinValueValidator
from user.models import User
from shared_model.basemodel import Basemodel

RATING_CHOICES = [
    (1, '1 - Poor'),
    (2, '2 - Fair'),
    (3, '3 - Good'),
    (4, '4 - Very Good'),
    (5, '5 - Excellent'),
]

class Category(Basemodel):
    """
    Model for categories
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
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='products'
                                 )

    class Meta:
        ordering = ['created_at']

    def average_rating(self):
        """
        Method to calculate the average rating of the product
        """
        return self.reviews.aggregate(AVG('rating')).get("rating", 0.0)

class Review(Basemodel):
    """
    Model for product reviews
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
    """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='wishlist')

class WishlistItem(Basemodel):
    """
    Model to store user wishlist items
    """
    wishlist = models.ForeignKey(Wishlist,
                                 on_delete=models.CASCADE,
                                 related_name="items")
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="items")