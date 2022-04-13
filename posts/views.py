from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    return HttpResponse('Главная страница')


def feed(request):
    return HttpResponse('Список объявлений')


def post_detail(request, post_id):
    responce = f'Детальное представление объявления #{post_id}'
    return HttpResponse(responce)


def post_edit(request, post_id):
    responce = f'Редактирование объявления #{post_id}'
    return HttpResponse(responce)


def post_create(request):
    return HttpResponse('Создание нового объявления')


def post_delete(request, post_id):
    responce = f'Удаление объявления #{post_id}'
    return HttpResponse(responce)


def post_favorite(request, post_id):
    responce = f'Объявление добавлено в избранное #{post_id}'
    return HttpResponse(responce)