from django.shortcuts import render,HttpResponseRedirect,get_object_or_404, redirect                      
from django.contrib import messages
from django.views import View
from django.views.generic.edit import UpdateView

from .models import Category, Item
from accounts.models import User, Merchant
from .forms import ProductForm

import random
from datetime import datetime

from rest_framework import generics
from rest_framework.response import Response
from .serializers import CategorySerializer, ItemSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView

# Create your views here.
class ProductListView(View):
    def get(self, request, *args, **kwargs):
        products = Item.objects.all()
        return render(request, 'product_list.html', {'products': products})
    

class CategoryDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        category = get_object_or_404(Category, slug=slug)
        products = Item.objects.filter(item_category=category)
        context = {'category': category, 'products': products}
        return render(request, 'category_detail.html', context)


class ProductDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Item, item_slug=slug)

        related_products = Item.filter_by_category(product.item_category).exclude(id=product.id)

        if len(related_products) >= 3:
            related_products = random.sample(list(related_products), 3)

        context = {'product': product, 'related_products': related_products}
        return render(request, 'product_detail.html', context)

class ProductCreateView(View):
    def get(self, request, id, *args, **kwargs):
        current_user = request.user.merchant
        current_merchant = get_object_or_404(Merchant, id=id)
        form = ProductForm()
        context = {'form': form, 'current_user': current_user, 'current_merchant': current_merchant}
        return render(request, 'product_create.html', context)

    def post(self, request, id, *args, **kwargs):
        current_user = request.user.merchant
        current_merchant = get_object_or_404(Merchant, id=id)
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.merchant
            post.save()

            messages.success(request, "Post Added Successfully!")
            return redirect('app:index')
        else:
            messages.error(request, "Error! Please Try Again.")

        context = {'form': form, 'current_user': current_user, 'current_merchant': current_merchant}
        return render(request, 'product_create.html', context)


class ProductUpdateView(UpdateView):
    model = Item
    template_name = 'product_update.html'
    form_class = ProductForm
    context_object_name = 'product'

    def form_valid(self, form):
        form.save()
        return redirect('product_detail', slug=self.object.item_slug)


# @method_decorator(login_required(login_url='/accounts/login/owner'), name='dispatch')
class ProductDeleteView(View):
    def get(self, request, id, *args, **kwargs):
        product = Item.objects.get(id=id)
        product.delete()
        messages.success(request, "Product Deleted Successfully!")
        return redirect('app:index')

class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [AllowAny]


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [AllowAny]


class CategoryDetailView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    # def put(self, request, slug):
    #     category = get_object_or_404(Category, slug=slug)
    #     serializer = CategorySerializer(category, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, slug):
    #     category = get_object_or_404(Category, slug=slug)
    #     category.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


