from django.db import models
from accounts.models import Customer
from product.models import Item
from django.utils import timezone

class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"
    
    def item_total(self):
        return self.item.item_price * self.quantity
    

class Cart(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    date_created = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Cart #{self.pk} - {self.user.user.email}'