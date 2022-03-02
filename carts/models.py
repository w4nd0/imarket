from django.db import models


class Cart(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0.0)

    user = models.OneToOneField("accounts.User", on_delete=models.PROTECT)
    products = models.ManyToManyField("products.Product", related_name="carts")
