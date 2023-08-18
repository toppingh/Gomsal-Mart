from django.db import models
from django.db.models import F, Case, When, Value

from accounts.models import Account
from shop.models import Product

class DeliveryBundle(models.Model):
    delivery_date = models.DateField(unique=True)

class Shipping(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=(
        ('in_transit', '배송 중'),
        ('delivered', '배송 완료'),
    ))
    delivery_date = models.DateField(null=True, blank=True)
    bundle = models.ForeignKey(DeliveryBundle, on_delete=models.CASCADE, related_name='shippings', null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.bundle:
            bundle, _ = DeliveryBundle.objects.get_or_create(delivery_date=self.delivery_date)
            self.bundle = bundle
            self.save(update_fields=['bundle'])  # Update only the 'bundle' field

    def __str__(self):
        return f"{self.product} - {self.status}"

    class Meta:
        ordering = ['-bundle__delivery_date', '-status']
