from django.urls import include, path

from .views import index
from accounts.views import (
    MerchantSignUpView,
    CustomerSignUpView,
    merchant_login_view,
    customer_login_view,
    logout_view
)
from product.views import (
    ProductListView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryDetailView
)
from cart.views import (
    AddToCartView,
    CartView,
    RemoveFromCartView,
    RemoveSingleItemFromCartView
)
from payment.views import make_payment
from order.views import create_order,order_list

urlpatterns = [
    # Home
    path('', index, name='index'),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/merchant/', MerchantSignUpView.as_view(), name='merchant_signup'),
    path('accounts/signup/customer/', CustomerSignUpView.as_view(), name='customer_signup'),
    path('accounts/login/merchant/', merchant_login_view, name='merchant_login'),
    path('accounts/login/customer/', customer_login_view, name='customer_login'),
    path('logout/', logout_view, name='logout'),

    # Product CRUD URLs
    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/create/<int:id>/', ProductCreateView.as_view(), name='product_create'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<slug:slug>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<slug:slug>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    # Cart
    path('add-to-cart/<slug:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('remove-from-cart/<slug:slug>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('remove-single-item-from-cart/<slug:slug>/', RemoveSingleItemFromCartView.as_view(), name='remove_single_item_from_cart'),

    # Category
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    
    # Payment
    path('make_payment/<int:order_id>/', make_payment, name='make_payment'),
    
    # orders
    path('create_order/', create_order, name='create_order'),
    path('orders/', order_list, name='order_list'),
]
