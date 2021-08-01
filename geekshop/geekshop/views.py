from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

def index(request):
    title = 'Контакты'
    context = {
        'title': title,
        'slogan': 'супер предложения',
    }

    return render(request, 'geekshop/index.html', context)


def contacts(request):
    return render(request, 'geekshop/contact.html')
