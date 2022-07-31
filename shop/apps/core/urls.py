from django.contrib import admin
from django.urls import path

from .views import index, category_list, category_detail, product_list, product_detail


app_name = 'core'


urlpatterns = [
    path('', index, name='index'),
    path('categories/', category_list, name='category_list'),
    path('categories/<slug>/', category_detail, name='category_detail'),
    path('products/', product_list, name='product_list'),
    path('products/<slug_category>/<pk>/', product_detail, name='product_detail')
]
