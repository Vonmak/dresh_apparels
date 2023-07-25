from django.db import models
from django.utils import timezone
from accounts.models import Customer
from order.models import Order

# Create your models here.
class Payment(models.Model):
    # user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    date_paid = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.user.email} paid {self.amount} on {self.date_paid}'

    class Meta:
        verbose_name_plural = 'Payments'

    def save(self, *args, **kwargs):
        self.amount = self.order.total_amount
        super().save(*args, **kwargs)
