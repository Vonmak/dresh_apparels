from django import forms

from .models import Item, Category



class ProductForm(forms.ModelForm):
    # item_category = forms.ChoiceField(Category, )
    class Meta:
        model = Item
        fields=['item_name','item_category','item_image','item_price','item_count', 'item_description']
        
    
    
        