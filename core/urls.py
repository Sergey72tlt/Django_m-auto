# from django.conf.urls import url
from django.urls import path
from .views import LoginView, SignUpView, ProfileView, logout_view

app_name = 'core'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:profile_id>', ProfileView.as_view(), name='profile-detail'),
]