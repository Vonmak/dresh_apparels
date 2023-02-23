from django.db import models
# from django.contrib.auth import get_user_model
from accounts.models import Customer
from cart.models import CartItem, Cart
from django.utils import timezone

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

    # def save(self, *args, **kwargs):
    #     # Calculate total amount based on cart items
    #     self.total_amount = sum([cart_item.item_total() for cart_item in self.items.all()])
    #     super().save(*args, **kwargs)
