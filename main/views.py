from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

# функции представления (контроллеры)

def index(request):
    categories = Categories.objects.all() # получение названий категорий приложения goods из модели categories
    context = {
        'title':'Home - Главная',
        'content':'Магазин мебели HOME',
        'categories':categories, # проброс категорий в html документ (чтобы они отображались на странице в меню)
    } # тестовый контент передаваемый в шаблон
    return render(request, "main/index.html",context) # подключение шаблона html (из папки templates)

def about(request):
    context = {
        'title':'Home - О нас',
        'content':'Магазин мебели HOME',
        'text':'Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн.',
    } # тестовый контент передаваемый в шаблон
    return render(request, "main/about.html",context)

def delivery(request):
    context = {
        'title':'Home - Доставка и оплата',
        'content':'Доставка и оплата',
        'text':'Доставка в этом магазине выполняется на транспорте, оплата принимается деньгами.'
    }
    return render(request, "main/delivery.html",context)

def contacts(request):
    context = {
        'title':'Home - Контакты',
        'content':'Контакты',
        'text':'Город Москва, +777 77 77'
    }
    return render(request, "main/contacts.html",context)
