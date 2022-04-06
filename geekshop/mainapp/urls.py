from django.urls import path
from .views import index
app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:pk>', index, name='product'),
    path('products_all/', index, name='products_all'),
    path('products_home/', index, name='products_home'),
    path('products_office/', index, name='products_office'),
    path('products_modern/', index, name='products_modern'),
    path('products_classic/', index, name='products_classic'),
]