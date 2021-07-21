import json
from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    title = 'Каталог'

    # with open('mainapp/templates/mainapp/json/categories.json', encoding='utf-8') as json_file:
    #    links_menu = json.load(json_file)

    # links_menu = [
    #     {'href': '', 'name': 'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'},
    # ]

    links_menu = ProductCategory.objects.all()

    products = Product.objects.all()[:4]

    context = {
        'title': title,
        'links_menu': links_menu,
        'related_products': products,
    }
    return render(request, 'mainapp/products.html', context)
