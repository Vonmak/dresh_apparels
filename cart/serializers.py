from rest_framework import serializers

from .models import CartItem, Cart
from product.serializers import ItemSerializer
from accounts.models import Customer

class CartItemSerializer(serializers.ModelSerializer):
    item= ItemSerializer()
    
    class Meta:
        model=CartItem
        fields= ('item','quantity')
        
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(read_only=True, many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    class Meta:
        model = Cart
        fields = ('user', 'items')
        