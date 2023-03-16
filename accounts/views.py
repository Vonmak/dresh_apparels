from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db import transaction
from django.contrib.auth import get_user_model,login,authenticate, logout
from django.urls import reverse_lazy

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny

from accounts.forms import *
from .serializers import MerchantSerializer, CustomerSerializer, LoginSerializer

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
    
def merchant_login_view(request):
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

def customer_login_view(request):
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

def logout_view(request):
    logout(request)
    return redirect('app:index')



@api_view(['POST'])
def create_merchant(request):
    serializer = MerchantSerializer(data=request.data)
    if serializer.is_valid():
        with transaction.atomic():
            user = get_user_model().objects.create(
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                email=serializer.validated_data['email'],
                is_merchant=True
            )
            user.set_password(serializer.validated_data['password1'])
            user.save()

            # Check if a Merchant with the given User already exists
            try:
                merchant = Merchant.objects.get(user=user)
                merchant.location = serializer.validated_data['location']
                merchant.save()
            except Merchant.DoesNotExist:
                merchant = Merchant.objects.create(user=user, location=serializer.validated_data['location'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        with transaction.atomic():
            user = get_user_model().objects.create(
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                email=serializer.validated_data['email'],
                is_customer=True
            )
            user.set_password(serializer.validated_data['password1'])
            user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
