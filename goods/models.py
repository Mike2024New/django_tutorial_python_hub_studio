from os import name
from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True,verbose_name='название') # поле с именем категории, макс длина 50 символов, должно быть уникальным
    slug = models.SlugField(max_length=50, unique=True, null=True,blank=True,verbose_name='url') # поле с url на категорию, уникальное, может быть пустым

    class Meta:
        db_table = "category" # здесь задаётся имя таблицы
        verbose_name = 'категорию' # отображение названия таблицы в админ панели в единственном числе
        verbose_name_plural = 'категории' # отображение названия таблицы в админ панели в множественном числе

    def __str__(self):
        """для того чтобы название категории корректно отображалось в админ панели""" # по умолчанию оно отображается по первичному ключу
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True,verbose_name='Название')
    slug = models.CharField(max_length=200, unique=True, blank=True,null=True,verbose_name='URL')
    description = models.TextField(blank=True,null=True,verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images',blank=True,null=True,verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2,verbose_name='Цена') # max_digits -> знаков до запятой, decimal_places -> знаков после запятой
    discount = models.DecimalField(default=0.00,max_digits=7, decimal_places=2,verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0,verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE,verbose_name='Категория') # привязка к категории таблицы Categories, если в той таблице есть ещё товары то при удалении категории в админ панели, будет задан вопрос удалить все товары или нет

    class Meta:
        db_table = 'product'
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self) -> str: # переопределение базовго метода класса модели, для корректного вывода названия товара при обращении к модели
        return f'{self.name} Количество - {self.quantity}'