from django.db import models

class Equipment(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
