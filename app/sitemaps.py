from django.contrib.sitemaps import Sitemap
from product.models import Category, Item

class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Category.objects.all()

class ItemSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Item.objects.all()
    
    def lastmod(self, obj):
        return obj.date_added