from django.urls import path
from main import views
from goods import views

app_name = "goods" # для ссылки на маршруты нужно задать имя текущему приложению

urlpatterns = [
    path('',view=views.catalog,name='index'),
    path('product/',view=views.product,name='product'),
]
