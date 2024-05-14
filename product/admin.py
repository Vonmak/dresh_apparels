from django.contrib import admin
from .models import Category, Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_description', 'item_price', 'item_count', 'date_added', 'user')
    list_filter = ('date_added', 'item_price', 'item_count','item_category')
    search_fields = ("item_name__startswith", )
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent_name')
    prepopulated_fields = {'slug': ('name',)}

    def parent_name(self, obj):
        if obj.parent:
            return obj.parent.name
        else:
            return '-'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
