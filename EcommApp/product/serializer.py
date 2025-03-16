from rest_framework import serializers
from .models import (Product,
                     Category,
                     Review,
                     Wishlist,
                     )

class CategorySerializer(serializers.Serializer):
    """
    Category Serializer Class

    Attributes:
        id (UUIDField): id of the category
        name (CharField): name of the category
        description (TextField): description of the category
        image (ImageField): image of the category
        created_at (DateTimeField): date and time the category was created
        updated_at (DateTimeField): date and time the category was updated
    """
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.TextField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        method to create a category
        """
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Updates the object based on the request data
        """
        for attr, value in validated_data:
            setattr(instance, attr, value)
        instance.save()

class ProductSerializer(serializers.Serializer):
    """
    Product Serializer Class

    Attributes:
        id (UUIDField): id of the product
        name (CharField): name of the product
        description (TextField): description of the product
        price (DecimalField): price of the product
        category (StringRelatedField): category of the product
        created_at (DateTimeField): date and time the product was created
        updated_at (DateTimeField): date and time the product was updated
        user (StringRelatedField): user that created the product
    """
    id  = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.TextField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    user = serializers.StringRelatedField()

    def create(self, validated_data):
        """
        method to create a product
        """
        return Product.objects.create(user=self.context.get('user_pk'),
                                      category=self.context.get('category_pk'),
                                        **validated_data)
    
    def update(self, instance, validated_data):
        """
        Updates the object based on the request data
        """
        for attr, value in validated_data:
            setattr(instance, attr, value)
        instance.save()

class ReviewSerializer(serializers.Serializer):
    """
    Review Serializer Class
    
    Attributes:
        id (UUIDField): id of the review
        product (StringRelatedField): product being reviewed
        user (StringRelatedField): user that created the review
        rating (PositiveSmallIntegerField): rating of the review
        comment (TextField): comment of the review
        created_at (DateTimeField): date and time the review was created
        updated_at (DateTimeField): date and time the review was updated
    """
    id = serializers.UUIDField(read_only=True)
    product = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    rating = serializers.PositiveSmallIntegerField()
    comment = serializers.TextField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        method to create a review
        """
        return Review.objects.create(user=self.context.get('user_pk'),
                                      product=self.context.get('product_pk'),
                                        **validated_data)

    
    def update(self, instance, validated_data):
        """
        Updates the object based on the request data
        """
        for attr, value in validated_data:
            setattr(instance, attr, value)
        instance.save()

    def validate(self, attrs):
        """
        Method to validate some attributes
        
        Args:
            attrs (dict): dictionary of attributes to be validated
        """
        product = self.context.get('product_pk')
        user = self.context.get('user_pk')

        if self.context["request"].method == "POST":
            if Review.objects.filter(product=product, user=user).exists():
                raise serializers.ValidationError("You have already reviewed this product")
        
        if not Product.objects.filter(pk=product).exists():
            raise serializers.ValidationError("Product does not exist")