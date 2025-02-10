#!/usr/bin/python3
"""Created by:
    Samuel Ezeh
    21/01/2025
"""

from uuid import uuid4
from datetime import datetime, UTC
from django.db import models

class Basemodel(models.Model):
    """Basemodel for all models"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the model"""
        return "{} - {}".format(self.__class__.__name__, self.id)
    
    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        if not self.id:
            self.id = uuid4()
        if not self.created_at:
            self.created_at = datetime.now(UTC)
        if not self.updated_at:
            self.updated_at = datetime.now(UTC)

    def save(self, *args, **kwargs):
        """
        Save method
        """
        self.updated_at = datetime.now(UTC)
        super().save(*args, **kwargs)

    def __eq__(self, other):
        """
        Equality method
        """
        return self.id == other.id
    
    def __ne__(self, other):
        """
        Inequality method
        """
        return self.id != other.id

    class Meta:
        abstract = True