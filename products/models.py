from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField()

