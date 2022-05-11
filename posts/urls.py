from django.urls import path
from .views import index, feed, post_detail, post_create, post_edit, post_delete, post_favorite


app_name ='posts'


urlpatterns = [
    path('', index, name='index'),
    path('feed/', feed, name='feed'),
    path('posts/<int:post_id>', post_detail, name='post-detail'),
    path('posts/<int:post_id>/edit/', post_edit, name='post-edit'),
    path('posts/<int:post_id>/delete/', post_delete, name='post-delete'),
    path('posts/<int:post_id>/favorite/', post_favorite, name='post-favorite'),
    path('posts/create/', post_create, name='post-create'),
]