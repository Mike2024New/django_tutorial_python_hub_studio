from django.http import HttpResponse
from django.shortcuts import render

# функции представления (контроллеры)

def index(request):
    context = {
        'title':'Home - Главная',
        'content':'Магазин мебели HOME'
    } # тестовый контент передаваемый в шаблон
    return render(request, "main/index.html",context) # подключение шаблона html (из папки templates)

def about(request):
    context = {
        'title':'Home - О нас',
        'content':'Магазин мебели HOME',
        'text':'Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн.',
    } # тестовый контент передаваемый в шаблон
    return render(request, "main/about.html",context)
