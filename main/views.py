from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context ={
        'title' : 'Home - Главная',
        'content' : "Магазин мебели HOME",
    }
    return render(request, 'main/index.html', context)

# видео на 2:10:15 
def about(request):
    context = {
        'title' : 'Home - О нас',
        'content' : 'О нас',
        'text_on_page' : 'Текст о том почему этот магазин такой классный, и какой хороший товар.',
    }
    return render(request, 'main/about.html',context)