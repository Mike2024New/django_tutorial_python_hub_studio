from django.shortcuts import get_list_or_404, render

from goods.models import Products

def catalog(request,category_slug):
    if category_slug == 'all':
        """на основании полученного url вернуть контент из БД"""
        goods = Products.objects.all() # получение товаров из БД
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    context = {
        'title':'Home - Каталог',
        'goods': goods,
    }
    return render(request,'goods/catalog.html',context)

def product(request,product_slug=False, product_id=False):
    """теперь по адресу categories/product/ можно искать товары по слагу и по идентификатору"""
    if product_id:
        product = Products.objects.get(id=product_id) # получаем из БД товар по заданному слагу (входному параметру)
    else:
        product = Products.objects.get(slug=product_slug) # получаем из БД товар по заданному слагу (входному параметру)
    context = {
        'product':product
    }
    return render(request, 'goods/product.html',context)
