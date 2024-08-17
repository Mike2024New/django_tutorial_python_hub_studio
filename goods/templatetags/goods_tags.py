from django import template
from goods.models import Categories

register = template.Library()

@register.simple_tag() # этот декоратор указывает что данная функция может быть загружена из html
def tag_categories():
    return Categories.objects.all() # получение названий категорий приложения goods из модели categories