from django.contrib.auth import authenticate
from django.contrib.auth import login, logout, get_user_model
from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render

import datetime

from profiles.forms import UserLoginForm, UserRegistrationForm, VerifyForm
from shop.models import *
#from .forms import UserForm
from django.http import *
from .models import *
User = get_user_model()


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    form = UserRegistrationForm(request.POST, request.FILES)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return render(request, 'users/register_done.html',
                      {'new_user': new_user})
    return render(request, 'users/register.html', {'form': form})


def delete_view(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            User.objects.get(pk=user.pk)
    return redirect('/')


def user_account(request):
    if not request.user.is_authenticated:
        return redirect('/')
    else:
        email = request.user
        user = User.objects.get(email=email)
        products = Product.objects.filter(author=user)

        return render(request, 'users/profile.html', {'user': user, 'products': products})


''' удаление данных из БД '''
def product_delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect('/')
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>ТОвар не найден</h2>")


def other_account(request, account_id):
    try:
        user = User.objects.get(id=account_id)
    except:
        raise Http404("Пользователь не найден!")
    user_posts = Product.objects.filter(author=user)

    return render(request, 'users/other_profile.html', {'user': user, 'user_posts': user_posts})


def verify_user(request):
    form = VerifyForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.pubdate = datetime.datetime.now()
            product.save()
            return redirect('/')

    return render(request, 'users/verify_form.html', {'form': form})


def style_list(request):
    users = User.objects.filter(is_verify=True)
    return render(request, 'shop/all_imagemakes.html', {'users': users})
