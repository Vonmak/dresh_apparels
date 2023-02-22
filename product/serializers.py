from rest_framework import serializers
from .models import Item, Category
from accounts.serializers import MerchantSerializer
from accounts.models import Merchant

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name', 'slug')

class ItemSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Merchant.objects.all())
    item_category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    
    class Meta:
        model = Item
        fields = ['user','item_name', 'item_description', 'item_image', 'item_price', 'item_count', 'item_category',]
