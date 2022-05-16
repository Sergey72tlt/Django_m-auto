from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.http import HttpResponse
from django.db.models import Count
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm


class IndexView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    LIMIT = 10

    def get_queryset(self):
        queryset = self.model.objects.annotate(
                                                favorite_nums=Count('favorite')
                                                ).order_by('-favorite_nums')[:self.LIMIT]
        return queryset


class FeedView(IndexView):

    @method_decorator(login_required(login_url='/admin/'))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        friends_list = self.request.user.profile.friends.all()
        queryset = Post.objects.filter(author__in=friends_list)
        return queryset


class PostDetail(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    pk_url_kwarg = 'post_id'
    comment_form = CommentForm
    comment_model = Comment

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=object)
        context['comments'] = self.get_comments()

        if request.user.is_authenticated:
            context['comment_form'] = self.comment_form
            return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = self.object
            comment.save()
            form = self.comment_form

        return render(request, self.template_name, context={'post': self.object, 'comments': self.get_comments(),
                                                            'comment_form': form})

    def get_comments(self):
        post = self.object
        comments = post.comments.all().order_by('-date_pub')
        return comments


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/detail.html', {'post': post})


def post_edit(request, post_id):
    responce = f'Редактирование объявления #{post_id}'
    return HttpResponse(responce)


@login_required(login_url='/admin/')
def post_create(request):
    form = PostForm()
    if request.method == 'GET':
        return render(request, 'posts/create.html', {'form': form})
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('posts:post-detail', kwargs={'post_id': post.id}))
        else:
            return render(request, 'posts/create.html', {'form':form})
    return HttpResponse('Создание нового объявления')


def post_delete(request, post_id):
    responce = f'Удаление объявления #{post_id}'
    return HttpResponse(responce)


@login_required(login_url='/admin/')
def post_favorite(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    if user in post.favorite.all():
        post.favorite.remove(user)
    else:
        post.favorite.add(user)
        post.save()
    return redirect(request.META.get('HTTP_REFERER'), request)