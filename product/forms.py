from django import forms

from .models import Item, Category

from cloudinary.forms import CloudinaryFileField


class ProductForm(forms.ModelForm):
    item_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    item_category = forms.ModelChoiceField(queryset=Category.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control'}))
    item_image = CloudinaryFileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    item_price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    item_count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    item_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        fields = ['item_name', 'item_category', 'item_image',
                  'item_price', 'item_count', 'item_description']


    
    
        