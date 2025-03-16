from django.urls import path
from .views import list_create, retrieve_update_delete

urlpatterns = [
    path("products?", list_create, name="list_create"),
    path("products/<str:pk>", retrieve_update_delete,
                              name="retrieve_update_delete"),
]
