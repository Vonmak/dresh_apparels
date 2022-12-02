from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Customer, Merchant, User
    
class MerchantForm(UserCreationForm):
    business_name = forms.CharField(label='Business Name',required=True)
    location = forms.CharField(label='Location',required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput, required=True)
    class Meta:
        model = User
        fields =('first_name','last_name','username','email','location')
        extra_kwargs = {'password1':{'write_only':True,'min_length':6}}

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_merchant = True
        user.save()
        merchant = Merchant.objects.get(user=user)
        merchant.business_name= self.cleaned_data.get('business_name')
        merchant.till_no= self.cleaned_data.get('till_no')
        merchant.location= self.cleaned_data.get('location')
        merchant.save()
        return user
    
class CustomerForm(UserCreationForm):
    name = forms.CharField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Password Confirm', widget=forms.PasswordInput, required=True)
    class Meta:
        model = User
        fields =('name','email')
        extra_kwargs = {'password1':{'write_only':True,'min_length':6}}

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.get(user=user)
        customer.name= self.cleaned_data.get('name')
        customer.save()
        return user
    
class MerchantLoginForm(forms.Form):
    username = forms.CharField()
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)
   
class CustomerLoginForm(forms.Form):
    username = forms.CharField()
    password=forms.CharField(max_length=20, widget=forms.PasswordInput)
