from django import forms
from .models import Item, Category
from cloudinary.forms import CloudinaryFileField

class ProductForm(forms.ModelForm):
    item_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    item_category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    item_image = CloudinaryFileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    item_price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}), min_value=0)
    item_count = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), min_value=0)
    item_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        fields = ['item_name', 'item_category', 'item_image', 'item_price', 'item_count', 'item_description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_category'].queryset = Category.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        item_price = cleaned_data.get('item_price')
        item_count = cleaned_data.get('item_count')

        if item_price is not None and item_price <= 0:
            self.add_error('item_price', 'Price must be greater than zero.')

        if item_count is not None and item_count <= 0:
            self.add_error('item_count', 'Count must be greater than zero.')
