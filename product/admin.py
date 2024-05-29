from django.contrib import admin
from .models import Category, Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'show_desc', 'item_price', 'item_count', 'date_added', 'user', 'item_category')
    list_filter = ('date_added', 'item_price', 'item_count', 'item_category')
    search_fields = ('item_name__startswith',)

class ReadOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]

admin.site.register(Category, ReadOnlyAdmin)
admin.site.register(Item, ItemAdmin)
