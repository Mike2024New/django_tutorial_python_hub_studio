from django.shortcuts import render

def catalog(request):
    context = {
        'title':'Home - Каталог',
        'goods': []
    }
    return render(request,'goods/catalog.html',context)

def product(request):
    context = {
        'title': '',
        
    }
    return render(request, 'goods/product.html')
