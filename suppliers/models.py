# models.py
from django.db import models

class Supplier(models.Model):
    brand = models.CharField(max_length=255)
    dealer = models.CharField(max_length=255)
    address = models.TextField()
    

    def __str__(self):
        return self.brand



