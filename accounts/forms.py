from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Customer, Merchant, User
    
class MerchantForm(UserCreationForm):
    location = forms.CharField(label='Location',required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput, required=True)
    class Meta:
        model = User
        fields =('first_name','last_name','email','location')
        extra_kwargs = {'password1':{'write_only':True,'min_length':6}}

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_merchant = True
        user.save()
        merchant = Merchant.objects.get(user=user)
        merchant.location= self.cleaned_data.get('location')
        merchant.save()
        return user
    
class CustomerForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput, required=True)
    class Meta:
        model = User
        fields =('first_name','last_name','email')
        extra_kwargs = {'password1':{'write_only':True,'min_length':6}}
    
class MerchantLoginForm(forms.Form):
    email = forms.EmailField()
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)
   
class CustomerLoginForm(forms.Form):
    email = forms.EmailField()
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)
