from django.shortcuts import render

from goods.models import Products

def catalog(request):
    goods = Products.objects.all() # получение товаров из БД

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
