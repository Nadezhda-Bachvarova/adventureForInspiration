from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from adventureProjectSia.accounts.forms import LoginForm, RegisterForm, ProfileForm


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = RegisterForm()
        context['profile_form'] = ProfileForm()
        return context

    @transaction.atomic
    def post(self, request):
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('home')

        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }

        return render(request, 'registration/signup.html', context)


def get_redirect_url(params):
    redirect_url = params.get('return_url')
    return redirect_url if redirect_url else 'home'


def signin_user(request):
    if request.method == 'GET':
        context = {
            'login_form': LoginForm(),
        }
        return render(request, 'registration/signin.html', context)
    else:
        login_form = LoginForm(request.POST)
        return_url = get_redirect_url(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(return_url)

        context = {
            'login_form': login_form,
        }

        return render(request, 'registration/signin.html', context)


@login_required
def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            'articles': user.userprofile.article_set.all(),
            'profile_pictures': user.userprofile.profile_image,
            'form': ProfileForm(),
        }
        return render(request, 'registration/user_profile.html', context)
    else:
        form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')

        return redirect('current user profile')


@login_required
def signout_user(request):
    logout(request)
    return redirect('home')
