from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages                       
from django.shortcuts import render, get_object_or_404, redirect                      
from django.views.generic import ListView, DetailView

from .models import Category, Item
from accounts.models import User, Merchant
from .forms import ProductForm
from cart.cart import Cart

import random
from datetime import datetime

# Create your views here.
def product_list(request):
    products=Item.objects.all()
    return render(request,'product_list.html', locals())

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    print(category)
    products = Item.objects.filter(item_category=category)
    
    print(products)
    
    return render(request, 'category_detail.html', locals())

def product_detail(request, slug):
    product = get_object_or_404(Item, item_slug=slug)

    related_products = Item.filter_by_category(product.item_category).exclude(id=product.id)
    print(related_products)
    
    if len(related_products) >= 3:
        related_products = random.sample(list(related_products), 3)

    return render(request, 'product_detail.html', locals())

def product_create(request, id):
    form=ProductForm()
    if request.method == 'POST':
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            post=form.save(commit=False)
            post.user= request.user.merchant
            post.save()

            messages.success(request, "Post Added Successfully!")
            return redirect('app:index')
        else:
            messages.error(request, "Error! Please Try Again.")
            return HttpResponseRedirect(request.path_info)
    else:
        form=ProductForm()
        
    return render(request,'product_create.html', locals())
            
def product_update(request, slug):
    product=Item.objects.get(item_slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('product_detail', product.id)
    else:
        form=ProductForm(instance=product)        
    return render(request,'product_update.html', locals())

# @login_required(login_url='/accounts/login/owner')
def product_delete(request, id):
  product = Item.objects.get(id=id)
  product.delete()
  messages.success(request, "Product Deleted Successfully!")
#   current_user= request.user
  return redirect('/')