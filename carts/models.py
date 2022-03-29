from django.db import models


class Cart(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    user = models.OneToOneField("accounts.User", null=True, on_delete=models.PROTECT)
    cart_owner = models.ForeignKey("accounts.User", null=True, on_delete=models.PROTECT, related_name='owner')
    products = models.ManyToManyField("products.Product", through='carts.CartProductShop')
    purchase = models.ManyToManyField("purchases.Purchase", related_name="cart", through='carts.CartProductShop')

class CartProductShop(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT)
    purchase = models.ForeignKey('purchases.Purchase', null=True, on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantity = models.IntegerField(default=1) 
