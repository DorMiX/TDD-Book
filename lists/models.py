from django.db import models

# Create your models here.


class List(models.Model):
    """List model."""

    pass


class Item(models.Model):
    """Item model."""
    
    text = models.TextField(default='')
    list = models.ForeignKey(List, default='')
