from django import template
from cart.models import Cart

register = template.Library()


@register.filter
def cart_item_count(user):
    if user is not None:
        qs = Cart.objects.filter(user=user)
        if qs.exists():
            return qs[0].items.count()
    return 0

@register.filter
def multiply(value, arg):
    return value * arg