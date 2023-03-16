from django.db import models
from django.utils import timezone

from accounts.models import Customer
from cart.models import CartItem

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customers')
    items = models.ManyToManyField(CartItem)
    date_created = models.DateTimeField(default=timezone.now)
    date_ordered = models.DateTimeField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'Order #{self.pk} - {self.user.user.email}'
