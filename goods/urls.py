from django.urls import path
from main import views
from goods import views

app_name = "goods" # для ссылки на маршруты нужно задать имя текущему приложению

urlpatterns = [
    path('',view=views.catalog,name='index'),
    path('product/<int:product_id>/',view=views.product,name='product'), # конвертация ссылки по полученному id (числовой маршрут размещать выше!)
    path('product/<slug:product_slug>/',view=views.product,name='product'), # конвертация ссылки по полученному слагу
]
