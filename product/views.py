from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages                       
from django.shortcuts import render, get_object_or_404, redirect                      
from django.views.generic import ListView, DetailView

from .models import Category, Item
from .forms import ProductForm

import random
from datetime import datetime

# Create your views here.
def product_list(request):
    products=Item.objects.all()
    return render(request,'product_list.html', locals())

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.items.filter(parent=None)

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'category_detail.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Item, item_slug=slug)
    # product.save()

    # related_products = list(product.item_category.items.filter(parent=None).exclude(id=product.id))
    
    # if len(related_products) >= 3:
    #     related_products = random.sample(related_products, 3)

    # if product.parent:
    #     return redirect('product_detail', category_slug=slug=product.parent.slug)

    return render(request, 'product_detail.html', locals())

def product_create(request):
    form=ProductForm()
    if request.method == 'POST':
        form=ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            # post=pform.save(commit=False)
            # post.user= request.user.Dog_Trainer
            form.save()

            messages.success(request, "Post Added Successfully!")
            return HttpResponseRedirect(request.path_info)
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