from django.shortcuts import get_object_or_404,render,redirect

from django.contrib import messages
from django.utils import timezone

from .cart import Cart
from product.models import Item
from order.models import OrderItem, Order


# Create your views here.
def add_to_cart(request, slug):
    item = get_object_or_404(Item, item_slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        # Check if item is in cart
        if order.items.filter(item__item_slug=item.item_slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.success(request, "Item quantity was updated")
            return redirect("app:index")

        else:
            messages.success(request, "Item was add to your cart")
            order.items.add(order_item)
            return redirect("app:index")

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        messages.success(request, "This item was add to your cart")

        order.items.add(order_item)

    return redirect("app:index")

def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )

    if order_qs.exists():
        order = order_qs[0]
        print('order', order)
        # Check if item is in cart
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.success(request, "This item was removed from your cart")
            return redirect("core:order-summery")
        else:
            messages.success(request, "This item is not in your cart")
            return redirect("core:product", slug=slug)
    else:
        # display message that order doesnt exist
        messages.danger(request, "Item doesnt exist")
        return redirect("core:product", slug=slug)
    
#removing a single item from cart
def remove_single_item_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )

    if order_qs.exists():
        order = order_qs[0]
        print('order', order)
        # Check if item is in cart
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity >1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.remove(order_item)
            messages.success(request, "This item quantity was updated")
            return redirect("core:order-summery")
        else:
            messages.success(request, "This item is not in your cart")
            return redirect("core:product", slug=slug)
    else:
        # display message that order doesnt exist
        messages.danger(request, "Item doesnt exist")
        return redirect("core:product", slug=slug)