from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django.contrib.auth import get_user_model

from .models import Customer, Merchant
from cloudinary.forms import CloudinaryFileField
import choices


class MerchantForm(UserCreationForm):
    location = forms.CharField(label='Location', required=True)
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Password Confirm', widget=forms.PasswordInput, required=True)

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'location')
        extra_kwargs = {'password1': {'write_only': True, 'min_length': 6}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_merchant = True
        user.save()
        merchant = Merchant.objects.get(user=user)
        merchant.location = self.cleaned_data.get('location')
        merchant.save()
        return user

class CustomerForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Password Confirm', widget=forms.PasswordInput, required=True)

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
        extra_kwargs = {'password1': {'write_only': True, 'min_length': 6}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'phone']
        widgets = {
            # Set email field as readonly
            'email': forms.EmailInput(attrs={'readonly': True})
        }


class MerchantProfileForm(forms.ModelForm):
    business_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    business_image = CloudinaryFileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    account_type = forms.ChoiceField(
        choices=choices.account_type,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    account_no = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    business_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Merchant
        fields = ['business_name', 'business_image',
                  'business_description', 'account_no', 'account_type', 'location']


class CustomerProfileForm(forms.ModelForm):
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = CloudinaryFileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Customer
        fields = ('image','bio', 'location')
