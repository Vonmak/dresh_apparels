from django.shortcuts import get_object_or_404,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, View

from .models import Cart, CartItem
from product.models import Item

# Create your views here.
class CartView(ListView):
    template_name = 'cart.html'
    context_object_name = 'items'

    def get_queryset(self):
        cart = Cart.objects.get(user=self.request.user.customer)
        items = cart.items.all()
        return items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = sum([item.item.item_price * item.quantity for item in context['items']])
        context['total'] = total
        return context
    
class AddToCartView(View):
    def post(self, request, slug, *args, **kwargs):
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


class RemoveFromCartView(LoginRequiredMixin, View):

    def get(self, request, slug, *args, **kwargs):
        item = get_object_or_404(Item, item_slug=slug)
        cart_qs = Cart.objects.filter(user=request.user.customer)

        if cart_qs.exists():
            cart = cart_qs[0]
            cart_item = CartItem.objects.filter(cart=cart, item=item)

            if cart_item.exists():
                cart_item.delete()
                messages.success(request, "This item was removed from your cart.")
            else:
                messages.warning(request, "This item is not in your cart.")
        else:
            messages.warning(request, "Cart does not exist.")
        
        return redirect("app:cart")

class RemoveSingleItemFromCartView(LoginRequiredMixin, View):

    def get(self, request, slug, *args, **kwargs):
        item = get_object_or_404(Item, item_slug=slug)
        order_item, created = CartItem.objects.get_or_create(item=item, cart__user=request.user.customer)
        
        if order_item.quantity > 1:
            order_item.quantity -= 1
            order_item.save()
        else:
            order_item.delete()
        
        return redirect(reverse('app:cart'))