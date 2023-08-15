from django.db import models

from accounts.models import Account
from shop.models import Product

class Shipping(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=(
        ('shipped', '발송됨'),
        ('in_transit', '배송 중'),
        ('delivered', '배송 완료'),
    ))
    delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product} - {self.status}"