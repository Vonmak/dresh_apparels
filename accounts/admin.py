from django.contrib import admin

from .models import Customer, Merchant, User

# Register your models here.
admin.site.register(User)
admin.site.register(Merchant)
admin.site.register(Customer)