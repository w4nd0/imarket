from django.db import models


class Cart(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    user = models.OneToOneField("accounts.User", on_delete=models.PROTECT)
    products = models.ManyToManyField("products.Product", through='carts.CartProductShop')
    purchase = models.ManyToManyField("purchases.Purchase", related_name="cart", through='carts.CartProductShop')

class CartProductShop(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    purchase = models.ForeignKey('purchases.Purchase', null=True, on_delete=models.PROTECT)
    unit_price = models.IntegerField()
    quantity = models.IntegerField(default=1) 
    total_item = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
