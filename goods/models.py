from enum import unique
from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True) # поле с именем категории, макс длина 50 символов, должно быть уникальным
    slug = models.SlugField(max_length=50, unique=True, null=True,blank=True) # поле с url на категорию, уникальное, может быть пустым

    class Meta:
        db_table = "category" # здесь задаётся имя таблицы