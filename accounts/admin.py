from django.contrib import admin

from .models import Customer, Merchant, User

# Register your models here.


class UserA(admin.ModelAdmin):
    list_display = ('email', 'id','first_name', 'last_name','phone','last_login','date_joined','is_customer','is_merchant','is_superuser',)
    list_filter = ('last_login', 'is_customer', 'is_merchant', 'is_superuser', 'date_joined')
    search_fields = ("first_name__startswith", )


class CusA(admin.ModelAdmin):
    list_display = ('user','id','date',)
    list_filter = ('date',)    

class MercA(admin.ModelAdmin):
    list_display = ('user','id', 'till_no', 'location', 'date',)
    list_filter = ('date',)
        
admin.site.register(User,UserA)
admin.site.register(Merchant,MercA)
admin.site.register(Customer, CusA)