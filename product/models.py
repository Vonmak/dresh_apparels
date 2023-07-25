from django.db import models
from django.shortcuts import reverse

from cloudinary.models import CloudinaryField
from accounts.models import Merchant
from .slug import unique_slugify

# Create your models here.
cat=[
        ('vehicles','vehicles'),
        ('property','property'),
        ('phones','phones'),
        ('electronics','electronics'),
        ('home','home'),
        ('beauty','beauty'),
        ('fashion','fashion'),
        ('sport','sport'),
        ('food','food'),
    ]
class Category(models.Model):
    name = models.CharField(max_length=255, choices=cat)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return '/%s/' % (self.name)
    
class Item(models.Model):
    user = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="item")
    item_name = models.CharField(max_length=50)
    item_slug = models.SlugField(max_length=255)
    item_description = models.TextField()
    item_image= CloudinaryField('image')
    item_price = models.FloatField()
    item_count = models.IntegerField()
    item_category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_added',)
        
    def __str__(self):
        return self.item_name
    
    def show_desc(self):
        return self.item_description[:50]
    
    def get_add_to_cart_url(self):
        return reverse("app:add-to-cart", kwargs={
            'slug': self.item_slug
        })

    def get_remove_from_cart_url(self):
        return reverse("app:remove-from-cart", kwargs={
            'slug': self.item_slug
        })
    
    def save(self, **kwargs):
        item_slug = '%s' % (self.item_name)
        unique_slugify(self, item_slug)
        super(Item, self).save()
        
    @classmethod
    def filter_by_category(self, item):
        cat = Item.objects.filter(item_category=item)
        return cat
