from django.shortcuts import render
from django.views.generic import View, DetailView
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .forms import LoginForm, SignupForm, UpdateProfileForm
from .models import Profile

MAIN_PAGE_URL = '/'


class LoginView(LoginView):
    template_name = 'core/login.html'
    form_class = LoginForm
    next_page = MAIN_PAGE_URL


class SignUpView(View):
    template_name = 'core/signup.html'
    form_class = SignupForm

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form_class
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(MAIN_PAGE_URL)
        else:
            return render(request, self.template_name, {'form': form})


class ProfileView(DetailView):
    profile = Profile
    template_name = 'core/profile.html'
    pk_url_kwarg = 'profile_id'


@login_required
def logout_view(request):
    logout(request)
    return redirect(MAIN_PAGE_URL)