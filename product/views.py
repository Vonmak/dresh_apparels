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
        
        # Retrieve all descendants of the selected category
        descendants = category.get_descendants()

        # Include the selected category itself
        descendants.append(category)

        # Retrieve all items belonging to the selected category and its descendants
        products = Item.objects.filter(item_category__in=descendants)
        
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
        current_merchant = self.get_merchant(request, id)
        products = Item.filter_by_owner(current_merchant)
        categories = self.get_category_tree()

        form = ProductForm()
        context = {
            'form': form,
            'current_user': request.user.merchant,
            'current_merchant': current_merchant,
            'products': products,
            'categories': categories 
        }
        return render(request, 'product_create.html', context)

    def post(self, request, id, *args, **kwargs):
        current_merchant = self.get_merchant(request, id)
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.user = request.user.merchant
                category_id = request.POST.get('item_category')
                post.item_category = Category.objects.get(id=category_id) if category_id else None  # Set selected category
                post.save()

                messages.success(request, "Post Added Successfully!")
                return redirect('app:index')
            except Decimal.InvalidOperation:
                messages.error(request, "Invalid price format. Please enter a valid decimal number.")
        else:
            error_messages = "\n".join([f"{field}: {', '.join(errors)}" for field, errors in form.errors.items()])
            messages.error(request, f"Error! Please correct the following errors:\n{error_messages}")

        categories = self.get_category_tree()

        context = {
            'form': form,
            'current_user': request.user.merchant,
            'current_merchant': current_merchant,
            'categories': categories 
        }
        return render(request, 'product_create.html', context)
    
    def get_category_tree(self):
        def build_tree(categories):
            tree = []
            for category in categories:
                node = {
                    'id': category.id,
                    'name': category.name,
                    'children': build_tree(category.children.all())
                }
                tree.append(node)
            return tree

        root_categories = Category.objects.filter(parent=None)
        return build_tree(root_categories)

    def get_merchant(self, request, id):
        return get_object_or_404(Merchant, id=id)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "You need to log in to create a product.")
            return redirect('login')
        if not hasattr(request.user, 'merchant'):
            messages.error(request, "You need to be a merchant to create a product.")
            return redirect('app:index')
        return super().dispatch(request, *args, **kwargs)

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



