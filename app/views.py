from django.shortcuts import render, get_object_or_404
from product.models import Category, Item

from datetime import datetime

def index(request):
    now = datetime.now()
    products = Item.objects.all()

    query = request.GET.get('query')
    category_slug = request.GET.get('category')  # Get the category slug from URL parameter

    if category_slug:  # If a category is selected
        category = get_object_or_404(Category, slug=category_slug)  # Get the category object
        products = products.filter(item_category=category)  # Filter items by the selected category

    if query:
        results = Item.search(query)
    else:
        results = None

    return render(request, 'index.html', {'products': products, 'results': results})

def about_page(request):
    return render(request, 'about.html')