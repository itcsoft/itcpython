
# Библиотека Django
from django.db import models


# Модель таблицы blog_todo
class Todo(models.Model):
    todo_name = models.CharField(max_length=300)

    class Meta:
        db_table = 'blog_todo'


# Модель таблицы blog_country
class Country(models.Model):
    country_name = models.CharField(max_length=300)
    
    class Meta:
        db_table = 'blog_country'

