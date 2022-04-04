# from django.conf.urls import url
from django.urls import path
from .views import index, posts

urlpatterns = [
    path('', index, name='index'),
]