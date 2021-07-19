from django.shortcuts import render


def index(request):
    title = 'Контакты'
    context = {
        'title': title,
        'slogan': 'супер предложения',
    }

    return render(request, 'geekshop/index.html', context)


def contacts(request):
    return render(request, 'geekshop/contact.html')
