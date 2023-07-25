from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.urls import reverse_lazy

from .models import Merchant, Customer
from .forms import MerchantForm, CustomerForm, LoginForm, MerchantProfileForm, CustomerProfileForm, UserForm


class MerchantSignUpView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    form_class = MerchantForm
    template_name = 'merchant_signup.html'
    success_url = reverse_lazy('app:login')
    success_message = '%(email)s Signed Up Successfully!'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'merchant'
        return super().get_context_data(**kwargs)


class CustomerSignUpView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    form_class = CustomerForm
    template_name = 'customer_signup.html'
    success_url = reverse_lazy('app:login')
    success_message = '%(email)s Signed Up Successfully!'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, username +
                                 " Logged In Successfully!")
                return redirect('app:index')
            else:
                messages.error(
                    request, "Username or Password is Incorrect. Please Try Again!")
                return redirect('app:login')
        else:
            return HttpResponse("Form is Not Valid")

    return render(request, 'login.html', locals())


def logout_view(request):
    logout(request)
    return redirect('app:index')


def merchant_profile(request):
    user = request.user
    merchant = user.merchant
    if not merchant:
        merchant = Merchant(user=user)
        merchant.save()

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        merchant_form = MerchantProfileForm(request.POST, request.FILES, instance=merchant)
        if merchant_form.is_valid():
            merchant_form.save()
            return redirect('app:merchant_profile')
        elif user_form.is_valid():
            user_form.save()
            return redirect('app:merchant_profile')
    else:
        user_form = UserForm(instance=user)
        merchant_form = MerchantProfileForm(instance=merchant)

    return render(request, 'merchant_profile.html', locals())


def customer_profile(request):
    user = request.user
    customer = user.customer
    if not customer:
        customer = Customer(user=user)
        customer.save()

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        customer_form = CustomerProfileForm(
            request.POST, request.FILES, instance=customer)
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            return redirect('app:customer_profile')
    else:
        user_form = UserForm(instance=user)
        customer_form = CustomerProfileForm(instance=customer)

    return render(request, 'customer_profile.html', locals())
