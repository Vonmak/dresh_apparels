from django.shortcuts import render
from product.models import Item, Category

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    object_list = Item.objects.all()
    menu_categories= Category.objects.all()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(object_list, 4)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    return render(request,'index.html',locals())