from django.shortcuts import render
from product.models import Category

# Create your views here.
def index(request):
    menu_categories = Category.objects.all()
    return render(request,'index.html',locals())