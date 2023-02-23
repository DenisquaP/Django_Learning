from django.shortcuts import render
from django.http import HttpResponseNotFound
from . import models


def index(request):
    ev = models.AppModel.objects.all()
    context = {
        'title': 'Главная страница',
        'info': ev
    }
    return render(request, 'app/index.html', context=context)  # noqa 501


def new_friend(request):
    return render(request, 'app/new_friend.html')


def chosed_friend(request, friend_name):
    context = {'friend_name': friend_name}
    return render(request, 'app/chosed.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Эту срань я сделал сам, но она не работает(</h1>')  # noqa 501
