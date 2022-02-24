from django.db import models


class Carts(models.Model):
    total = models.DecimalField()

    user = models.OneToOneField("accounts.User", on_delete=models.PROTECT, null=True)
    products = models.ManyToManyField("products.Product", related_name="carts")
