from django.contrib import admin

from .models import Cart, CartItem
# Register your models here.
class CartItemA(admin.ModelAdmin):
    list_display = ('item', 'quantity',)
admin.site.register(Cart)
admin.site.register(CartItem, CartItemA)