import json
from django.shortcuts import render


def index(request):
    title = 'Каталог'

    with open('mainapp/templates/mainapp/json/categories.json', encoding='utf-8') as json_file:
        links_menu = json.load(json_file)

    # links_menu = [
    #     {'href': 'index', 'name': 'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'},
    # ]

    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context)
