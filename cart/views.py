from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse

from django.contrib import messages
from django.utils import timezone

from .models import Cart, CartItem
from product.models import Item

from django.urls import reverse


# Create your views here.
def cart(request):
    cart = Cart.objects.get(user=request.user.customer)
    items = cart.items.all()
    total = 0
    for item in items:
        total += item.item.item_price * item.quantity
    
    return render(request, 'cart.html', {'items': items, 'total': total})

def add_to_cart(request, slug):
    item = get_object_or_404(Item, item_slug=slug)
    cart_qs = Cart.objects.filter(user=request.user.customer)

    if cart_qs.exists():
        cart = cart_qs[0]
        cart_item, created = cart.items.get_or_create(
            item=item,
            defaults={'quantity': 1},
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, "Item quantity was updated")
        else:
            messages.success(request, "Item was added to your cart")
    else:
        cart = Cart.objects.create(user=request.user.customer)
        cart_item, created = cart.items.get_or_create(
            item=item,
            defaults={'quantity': 1}
        )
        cart.items.add(cart_item)
        messages.success(request, "Item was added to your cart")

    return redirect("app:cart")


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, item_slug=slug)
    cart_qs = Cart.objects.filter(user=request.user.customer)
    
    if cart_qs.exists():
        cart = cart_qs[0]
        cart_item = CartItem.objects.filter(item=item)
        
        if cart_item.exists():
            cart.items.all().delete()
            cart_item.delete()
            messages.success(request, "This item was removed from your cart.")
            return redirect("app:cart")
        else:
            messages.success(request, "This item is not in your cart.")
            return redirect("app:product", slug=slug)
    else:
        messages.danger(request, "Cart does not exist.")
        return redirect("app:product", slug=slug)

def remove_single_item_from_cart(request, item_slug):
    item = get_object_or_404(Item, item_slug=item_slug)
    order_item, created = CartItem.objects.get_or_create(item=item)
    
    if order_item.quantity > 1:
        order_item.quantity -= 1
        order_item.save()
    else:
        order_item.delete()
        
    return redirect(reverse('app:cart'))
