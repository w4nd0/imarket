from django.db import models


class Purchases(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT, null=True)
    cart = models.ForeignKey("carts.Cart", on_delete=models.PROTECT, null=True)
