from django.shortcuts import render
from product.models import Category, Item

# Create your views here.
def index(request):
    menu_categories = Category.objects.all()
    products=Item.objects.all()
    return render(request,'index.html',locals())