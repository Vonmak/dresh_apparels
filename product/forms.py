from django import forms

from .models import Item



class ProductForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=['item_name','item_image','item_price','item_count', 'item_description']
        
    
    
        