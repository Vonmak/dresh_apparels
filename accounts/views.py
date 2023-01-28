from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from accounts.forms import *
# from accounts.models import User
from django.contrib.auth import get_user_model

from django.contrib.auth import login,authenticate, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class MerchantSignUpView(SuccessMessageMixin,CreateView):
    model = get_user_model()
    form_class = MerchantForm
    template_name = 'merchant_signup.html'
    success_url =reverse_lazy('app:merchant_login')
    success_message = '%(email)s Signed Up Successfully!'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'merchant'
        return super().get_context_data(**kwargs)
    
class CustomerSignUpView(SuccessMessageMixin,CreateView):
    model = get_user_model()
    form_class = CustomerForm
    template_name = 'customer_signup.html'
    success_url =reverse_lazy('app:customer_login')
    success_message = '%(email)s Signed Up Successfully!'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)
    
def merchantloginView(request):
    form=MerchantLoginForm()
    if request.method=='POST':
        form=MerchantLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, username + " Logged In Successfully!")
                return redirect('app:index')
            else:
                messages.error(request, "Username or Password is Incorrect. Please Try Again!")
                return redirect('app:merchant_login')
        else:
            return HttpResponse("Form is Not Valid")
    
    return render(request,'merchant_login.html',locals())

def customerloginView(request):
    form=CustomerLoginForm
    if request.method=='POST':
        form=CustomerLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, username + " Logged In Successfully!")
                return redirect('app:index')
            else:
                messages.error(request, "Username or Password is Incorrect. Please Try Again!")
                return redirect("app:customer_login")
        else:
            return HttpResponse("Form is Not Valid")
    
    return render(request,'customer_login.html',locals())

def logout_user(request):
    logout(request)
    return redirect('app:index')