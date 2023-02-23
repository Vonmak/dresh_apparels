from django.urls import path

from accounts.views import create_merchant, create_customer, LoginView
from product.views import ItemList, CategoryDetailView, ItemDetail
from cart.views import CartList, CartItemList,RemoveSingleItemFromCartViews



urlpatterns = [
    path('merchants/', create_merchant),
    path('customers/', create_customer),
    path('users/login/', LoginView.as_view()),
    path('items/', ItemList.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartList.as_view(), name='cart'),
    path('cartitem/', CartItemList.as_view(), name='cartitem'),
    
    path('cart/remove/<slug:item_slug>/', RemoveSingleItemFromCartViews.as_view(), name='remove_single_item_from_cart'),
    
]