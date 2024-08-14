from django.contrib import admin

# Register your models here.
from goods.models import Categories,Products

# простой способ регистрации модели в админской панели (отключен)
# admin.site.register(Categories) # чтобы модель появилась на админ панели нужно передать её в регистр
# admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """этот класс отвечает за то как названия модели будут отображаться в панели администратора
    prepopulated_fields - поможет создать название url, пользователь будет вводить название категории кириллицей, а это свойство 
    переведет его в латиницу и подставит в поле slug
    """
    prepopulated_fields = {'slug':('name',)} # то есть текст введенный в name, подставится в slug в латинице


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)} # то есть текст введенный в name, подставится в slug в латинице