from django.shortcuts import render
from product.models import Item, Category

# Create your views here.
def index(request):
    object_list = Item.objects.all()
    menu_categories= Category.objects.filter(parent=None)
    return render(request,'index.html',locals())