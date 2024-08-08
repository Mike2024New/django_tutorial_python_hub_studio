from django.http import HttpResponse
from django.shortcuts import render

# функции представления (контроллеры)

def index(request):
    context = {
        'title':'Home',
        'content':'Главная страница магазина - HOME',
        'list':['first','second'],
        'dict':{'first':1},
        'bool':True # эта переменная управляет отображением данных на шаблоне
    } # тестовый контент передаваемый в шаблон
    return render(request, "main/index.html",context) # подключение шаблона html (из папки templates)

def about(request):
    return HttpResponse(content="about page")
