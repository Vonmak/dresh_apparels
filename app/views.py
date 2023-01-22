from django.shortcuts import render
from product.models import Item, Category

# Create your views here.
def index(request):
    object_list = Item.objects.all()
    menu_categories= Category.objects.all()
    return render(request,'index.html',locals())