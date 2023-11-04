from django.db import models

class Category(models.Models):
    name = models.CharField(max_length = 30, unique = True)
    description = models.TextField()
