from django.db import models


class Purchase(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT, null=True)
