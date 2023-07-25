from django.contrib import admin

from .models import *

# Register your models here.
class ItemA(admin.ModelAdmin):
    list_display = ('item_name', 'item_description', 'item_price', 'item_count', 'date_added','user')
    list_filter = ('date_added','item_price', 'item_count')
    search_fields = ("item_name__startswith", )


class CatA(admin.ModelAdmin):
    list_display = ('name','slug')
admin.site.register(Category, CatA)
admin.site.register(Item, ItemA)