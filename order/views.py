from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order
from cart.models import Cart

def create_order(request):
    cart = Cart.objects.get(user=request.user.customer)
    items = cart.items.all()
    print([item.item.item_price for item in items])
    order_qs=Order.objects.filter(user=request.user.customer)
    print(order_qs)
    # if order_qs.exists():
    #     cart = order_qs[0]
    #     cart_item, created = cart.items.get_or_create(
    #         item=item,
    #         defaults={'quantity': 1},
    #     )
    #     if not created:
    #         cart_item.quantity += 1
    #         cart_item.save()
    #         messages.success(request, "Item quantity was updated")
    #     else:
    #         messages.success(request, "Item was added to your cart")
                
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

# def post(self, request, slug, *args, **kwargs):
#         item = get_object_or_404(Item, item_slug=slug)
#         cart_qs = Cart.objects.filter(user=request.user.customer)

#         if cart_qs.exists():
#             cart = cart_qs[0]
#             cart_item, created = cart.items.get_or_create(
#                 item=item,
#                 defaults={'quantity': 1},
#             )
#             if not created:
#                 cart_item.quantity += 1
#                 cart_item.save()
#                 messages.success(request, "Item quantity was updated")
#             else:
#                 messages.success(request, "Item was added to your cart")
#         else:
#             cart = Cart.objects.create(user=request.user.customer)
#             cart_item, created = cart.items.get_or_create(
#                 item=item,
#                 defaults={'quantity': 1}
#             )
#             cart.items.add(cart_item)
#             messages.success(request, "Item was added to your cart")

#         return redirect("app:CartView")