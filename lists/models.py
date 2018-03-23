from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class List(models.Model):
    """List model."""

    def get_absolute_url(self):
        """Get absolute URL."""
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    """Item model."""

    text = models.TextField(default='')
    list = models.ForeignKey(List, default='')
