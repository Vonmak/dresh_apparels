from .models import Category

def categories(request):
    menu_categories = Category.objects.filter(parent=None)
    return {'menu_categories': menu_categories,}
