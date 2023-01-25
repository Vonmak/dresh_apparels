from django.urls import include, path

from .views import *
from accounts.views import *
from product.views import *
from cart.views import *


urlpatterns = [
    path('', index, name='index'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/merchant', MerchantSignUpView.as_view(), name='merchant_signup'),
    path('accounts/signup/customer', CustomerSignUpView.as_view(), name='customer_signup'),
    path('accounts/login/merchant', merchantloginView, name='merchant_login'),
    path('accounts/login/customer', customerloginView, name='customer_login'),
    path('logout/', logout_user, name='logout'),
    
    #Product CRUD urls
    path('products/', product_list, name='products'), #view all products
    path('product/<int:id>/create/', product_create, name='product_create'), #create a new product
    path('product/<slug:slug>/', product_detail, name='product_detail'), #view a single product
    path('product/<slug:slug>/update/', product_update, name='product_update'), #update a new product
    path('product/delete/<id>', product_delete, name='product_delete'), #delete a product
    
    #Category
    path('<slug:slug>/', category_detail, name='category_detail'),
    
    #Add to cart
    # path('cart/<int:product_id>/', add_to_cart, name='add_to_cart')
    path('add-to-cart/<slug:slug>/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug:slug>/', remove_from_cart, name="remove-from-cart"),
    path('remove-single-item-cart/<slug:slug>',remove_single_item_cart, name='remove-single-item-cart'),
    
    
    
    # path('product/<slug:slug>/', ProductView.as_view(), name='product'),
    # path('products/', ProductsView.as_view(), name='products'),
    # path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    # path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart')

]