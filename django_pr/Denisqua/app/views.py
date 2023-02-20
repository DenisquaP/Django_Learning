from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse
from . import models


def index(request):
    ev = models.AppModel.objects.all()
    context = {
        'title': 'Главная страница',
        'info': ev
    }
    return render(request, 'app/index.html', context=context)  # noqa 501


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Эту срань я сделал сам, но она не работает(</h1>')  # noqa 501


def new_friend(request):
    return HttpResponse('<h1>Добавь нового друга</h1>')
