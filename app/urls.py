# from django.urls import include, path

# from .views import index
# from accounts.views import MerchantSignUpView, CustomerSignUpView, merchantloginView, customerloginView, logout_user
# from product.views import product_list, product_create, product_detail, product_update, product_delete, category_detail
# from cart.views import add_to_cart, cart, remove_from_cart, remove_single_item_from_cart, CartView
# # from order.views import generate_order, view_order


# urlpatterns = [
#     # Home
#     path('', index, name='index'),
    
#     # Accounts
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('accounts/signup/merchant', MerchantSignUpView.as_view(), name='merchant_signup'),
#     path('accounts/signup/customer', CustomerSignUpView.as_view(), name='customer_signup'),
#     path('accounts/login/merchant', merchantloginView, name='merchant_login'),
#     path('accounts/login/customer', customerloginView, name='customer_login'),
#     path('logout/', logout_user, name='logout'),
    
#     #Product CRUD urls
#     path('products/', product_list, name='products'), #view all products
#     path('product/<int:id>/create/', product_create, name='product_create'), #create a new product
#     path('product/<slug:slug>/', product_detail, name='product_detail'), #view a single product
#     path('product/<slug:slug>/update/', product_update, name='product_update'), #update a new product
#     path('product/delete/<id>', product_delete, name='product_delete'), #delete a product

#     # Order
#     # path('generate-order/', generate_order, name='generate_order'), #generate a new order
#     # path('order/<int:order_id>/', view_order, name='view_order'), 
    
    
#     # Cart
#     path('add_to_cart/<slug:slug>/', add_to_cart, name='add_to_cart'),
#     path('cart/', cart, name='cart'),
#     path('remove_from_cart/<slug:slug>/', remove_from_cart, name='remove_from_cart'),
#     path('remove_single_item_from_cart/<slug:item_slug>/', remove_single_item_from_cart, name='remove_single_item_from_cart'),
    
#     path('cartview/', CartView.as_view(), name='cart_view'),

    
#     #Category
#     path('<slug:slug>/', category_detail, name='category_detail'),  

# ]


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
