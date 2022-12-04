from django.urls import include, path

from .views import *
from accounts.views import *
from product.views import *

urlpatterns = [
    path('', index, name='index'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/merchant', MerchantSignUpView.as_view(), name='merchant_signup'),
    path('accounts/signup/customer', CustomerSignUpView.as_view(), name='customer_signup'),
    path('accounts/login/merchant', merchantloginView, name='merchant_login'),
    path('accounts/login/customer', customerloginView, name='customer_login'),
    path('logout/', logout_user, name='logout'),

    # path('', include(('product.urls','product'), namespace='product')),
    # path('', HomeView.as_view(), name='home'),
    # path('', home, name='home'),
    # path('product/<pk>/', ProductView.as_view(), name='product'),
    # path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    # path('<slug:slug>/', category_detail, name='category_detail'),
    # path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    # path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart')
]