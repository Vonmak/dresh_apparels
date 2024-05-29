from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'

    def ready(self):
        super().ready()
        from .categories import CATEGORIES
        from .models import Category
        
        @receiver(post_migrate, sender=self)
        def create_predefined_categories(sender, **kwargs):
            if sender.name == 'product':  # Replace 'product' with the actual name of your app
                def create_categories(categories, parent=None):
                    for cat in categories:
                        category, created = Category.objects.get_or_create(name=cat['name'], slug=cat['slug'], parent=parent)
                        create_categories(cat.get('children', []), category)

                create_categories(CATEGORIES)
