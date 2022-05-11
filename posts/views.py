from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from .models import Post


def index(request):
    posts = Post.objects.annotate(favorite_nums=Count('favorite')).order_by('favorite_nums')[:10]
    context = {
        'popular_posts': posts
    }
    return render(request, 'posts/index.html', context)


def feed(request):
    posts = Post.objects.filter(author__in=request.user.profile.friends.all())
    responce = [f'id: {post.id}| author: {post.author}' for post in posts]
    return HttpResponse(responce)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/detail.html', {'post': post})


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