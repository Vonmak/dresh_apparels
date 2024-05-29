from django.db import models
from django.shortcuts import reverse

from django.db.models import Q  # Import Q object

from cloudinary.models import CloudinaryField
from accounts.models import Merchant
from .slug import unique_slugify

from decimal import Decimal
from django.core.validators import MinValueValidator

from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

    def get_absolute_url(self):
        return '/%s/' % (self.slug)

    def get_descendants(self):
        descendants = []
        self._get_descendants(descendants)
        return descendants

    def _get_descendants(self, descendants):
        children = self.children.all()
        for child in children:
            descendants.append(child)
            child._get_descendants(descendants)
        return descendants
    
class Item(models.Model):
    user = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="items")
    item_name = models.CharField(max_length=50)
    item_slug = models.SlugField(max_length=255)
    item_description = models.TextField()
    item_image= CloudinaryField('image')
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_count = models.IntegerField(validators=[MinValueValidator(0)])
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

    def get_absolute_url(self):
        return reverse('app:product_detail', kwargs={'slug': self.item_slug})

    def save(self, *args, **kwargs):
        if not self.item_slug:
            unique_slugify(self, self.item_name)
        super(Item, self).save(*args, **kwargs)


    @classmethod
    def filter_by_category(cls, category):
        return cls.objects.filter(item_category=category)

    @classmethod
    def filter_by_owner(cls, owner):
        return cls.objects.filter(user=owner)

    
    @classmethod
    def search(cls, query):
        return cls.objects.filter(
            Q(item_category__name__icontains=query) |
            Q(item_name__icontains=query)
        ).distinct()