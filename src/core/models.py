from django.db import models


class Base(models.Model):
    """Base model for every other within this project
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'core'
        abstract = True
