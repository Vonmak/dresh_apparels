from django.shortcuts import render,get_object_or_404, redirect                      
from django.contrib import messages
from django.views import View

from .models import Category, Item
from accounts.models import Merchant
from cart.models import CartItem
from .forms import ProductForm

import random

# Create your views here.
class ProductListView(View):
    def get(self, request, *args, **kwargs):
        products = Item.objects.all()
        return render(request, 'product_list.html', {'products': products})
    

class CategoryDetail(View):
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
            # Collect form errors and display them
            error_messages = "\n".join([f"{field}: {error}" for field, error in form.errors.items()])
            messages.error(request, f"Error! Please correct the following errors:\n{error_messages}")

        context = {'form': form, 'current_user': current_user, 'current_merchant': current_merchant}
        return render(request, 'product_create.html', context)


class ProductUpdateView(View):
    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Item, item_slug=slug)
        form = ProductForm(instance=product)
        context = {'form': form, 'product': product}
        return render(request, 'product_update.html', context)

    def post(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Item, item_slug=slug)
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            product = form.save()

            messages.success(request, "Product Updated Successfully!")
            return redirect('app:product_detail', slug=product.item_slug)
        else:
            messages.error(request, "Error! Please Try Again.")

        context = {'form': form, 'product': product}
        return render(request, 'product_update.html', context)




# @method_decorator(login_required(login_url='/accounts/login/owner'), name='dispatch')
class ProductDeleteView(View):
    def get(self, request, id, *args, **kwargs):
        product = get_object_or_404(Item, id=id)
        product.delete()
        messages.success(request, "Product Deleted Successfully!")
        return redirect('app:index')



