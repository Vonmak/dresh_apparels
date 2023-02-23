from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order
from cart.models import Cart
# Create your views here.

def create_order(request):
    cart = Cart.objects.get(user=request.user.customer)
    items = cart.items.all()
                
    total_amount = sum([item.item.item_price for item in items])
    print(total_amount)
    order = Order.objects.create(user=request.user.customer, total_amount=total_amount)
    order.items.set(items)
    cart.items.clear()
    messages.success(request, 'Your order has been placed successfully.')
    return redirect('app:order_list')

def order_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders.html', context)
