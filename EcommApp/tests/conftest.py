import pytest
from user.models import (
    User,
    UserProfile
)
from product.models import (
    Product,
    ProductCategory,
    ProductReview,
    Wishlist
)

@pytest.fixture
def User() -> User:
    """
    Creates a test user for the test cases
    """
    return User.objects.create_user(username="test_user",
                                    password="testpasswd"
                                    )

@pytest.fixture
def UserProfile(User) -> UserProfile:
    """
    Creates a test user profile for the test cases
    """
    return UserProfile.objects.create(user=User,
                                      first_name="test",
                                      last_name="user",
                                      phone_number="1234567890",
                                      address="test address",
                                      date_of_birth="2021-01-01"
                                      )

@pytest.fixture
def ProductCategory() -> ProductCategory:
    """
    Creates a test product category for the test cases
    """
    return ProductCategory.objects.create(name="test_category",
                                          description="test description"
                                          )

@pytest.fixture
def Product(User, ProductCategory) -> Product:
    """
    Creates a test product for the test cases
    """
    return Product.objects.create(name="test_product",
                                  description="test description",
                                  price=100.00,
                                  quantity=10,
                                  user_id=User,
                                  category_id=ProductCategory
                                  )
@pytest.fixture
def ProductReview(User, Product) -> ProductReview:
    """
    Creates a test product review for the test cases
    """
    return ProductReview.objects.create(product_id=Product,
                                        user_id=User,
                                        rating=5,
                                        review="test review"
                                        )

@pytest.fixture
def Wishlist(User, Product) -> Wishlist:
    """
    Creates a test wishlist for the test cases
    """
    return Wishlist.objects.create(user_id=User,
                                   product_id=Product
                                   )