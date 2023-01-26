from django.db import models
from accounts.models import User
from product.models import Item
from django.utils import timezone

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_created = models.DateTimeField(default=timezone.now)