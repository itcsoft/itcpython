"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    # Путь Главная страница
    path('', views.home),

    # Путь О Нас
    path('about/', views.about),
    # Путь Time
    path('time/', views.time),
    # Путь мой кошелек
    path('wallet/', views.mywallet),

    # TODO CRUD
    path('todo/', views.todo),
    path('todo-add/', views.todo_add),
    path('todo-delete/', views.todo_delete),

    # COUNTRY CRUD
    path('countries/', views.countries),
    path('country-add/', views.country_add),

    # Путь Админовая часть
    path('admin/', admin.site.urls),
]
