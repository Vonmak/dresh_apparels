from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from .managers import CustomUserManager
from cloudinary.models import CloudinaryField

# Create your models here.
class User(AbstractUser):
    is_merchant = models.BooleanField('merchant', default=False)
    is_customer = models.BooleanField('customer', default=True)
    phone= models.CharField(max_length=10)
    email = models.EmailField(('email address'), unique=True) # changes email to unique and blank to false
    username = None
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS
    
class Merchant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="merchant")
    image = CloudinaryField('image')
    till_no = models.IntegerField(blank=True, null=True)
    location= models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    @receiver(post_save, sender=User)
    def create_user(sender, instance, created, dispatch_uid="merchant", **kwargs):
        if instance.is_merchant:
            if created:
                Merchant.objects.get_or_create(user = instance)

    @receiver(post_save, sender=User)
    def save_admin(sender, instance, **kwargs):
        if instance.is_merchant:
            instance.merchant.save()

    def save_profile(self):
        self.save()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    image = CloudinaryField('image')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    @receiver(post_save, sender=User)
    def create_user(sender, instance, created, dispatch_uid="customer", **kwargs):
        if instance.is_customer:
            if created:
                Customer.objects.get_or_create(user = instance)

    @receiver(post_save, sender=User)
    def save_admin(sender, instance, **kwargs):
        if instance.is_customer:
            instance.customer.save()

    def save_profile(self):
        self.save()
 