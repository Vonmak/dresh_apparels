from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import Payment
from order.models import Order

# Create your views here.

@login_required
def make_payment(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    
    if request.method == 'POST':
        # create a new Payment object and set its attributes
        payment = Payment()
        payment.user = request.user.customer
        payment.order = order
        payment.date_paid = timezone.now()
        payment.save()
        
        # update the corresponding Order object
        order.date_ordered = timezone.now()
        order.is_ordered = True
        order.save()
        
        return HttpResponseRedirect('/orders/')  # redirect to the orders page
    
    context = {'order': order}
    return render(request, 'make_payment.html', context)
