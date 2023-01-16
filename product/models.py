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
    # parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, choices=cat)
    # slug = models.SlugField(max_length=255)
    # ordering = models.IntegerField(default=0)
    # is_featured = models.BooleanField(default=False)

    # class Meta:
    #     verbose_name_plural = 'Categories'
    #     ordering = ('ordering',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return '/%s/' % (self.name)
class Item(models.Model):
    user = models.ForeignKey(Merchant, on_delete=models.CASCADE, related_name="item")
    # parent = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    item_name = models.CharField(max_length=50)
    item_slug = models.SlugField(max_length=255)
    item_description = models.TextField()
    item_image= CloudinaryField('image')
    item_price = models.FloatField()
    item_count = models.IntegerField()
    item_category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    # item_category = models.CharField(max_length=255, choices=cat)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_added',)
        
    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse("app:product_detail", kwargs={
            "pk" : self.pk
        })

    def get_add_to_cart_url(self) :
        return reverse("app:add-to-cart", kwargs={
            "pk" : self.pk
        })

    def get_remove_from_cart_url(self) :
        return reverse("app:remove-from-cart", kwargs={
            "pk" : self.pk
        })
    
    def save(self, **kwargs):
        item_slug = '%s' % (self.item_name)
        unique_slugify(self, item_slug)
        super(Item, self).save()
        
    @classmethod
    def category(self, item):
        cat = Item.objects.filter(item_category=item)
        return cat
