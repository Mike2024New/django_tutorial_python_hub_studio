from django.shortcuts import render

from goods.models import Products

def catalog(request):
    goods = Products.objects.all() # получение товаров из БД

    context = {
        'title':'Home - Каталог',
        'goods': goods,
    }
    return render(request,'goods/catalog.html',context)

def product(request):
    context = {
        'title': '',
        
    }
    return render(request, 'goods/product.html')
