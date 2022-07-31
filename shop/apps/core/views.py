from django.shortcuts import render
from .models import Category, Product, Tag


def index(request):
    context = {}
    category_qs = Category.objects.all()
    product_qs = Product.objects.all().order_by('title')[:3]

    context['category_list'] = category_qs
    context['product_list'] = product_qs

    return render(request, 'core/index.html', context)


def category_list(request):
    context = {}
    category_qs = Category.objects.all()
    context['category_list'] = category_qs
    return render(request, 'core/category_list.html', context)


def category_detail(request, slug):
    context = {}
    category = Category.objects.filter(slug=slug).first()
    context['category'] = category
    print(category)
    return render(request, 'core/category.html', context)


def product_list(request):
    context = {}
    product_qs = Product.objects.all()
    context['product_list'] = product_qs
    return render(request, 'core/product_list.html', context)


def product_detail(request, slug_category, pk):
    context = {}
    product = Product.objects.filter(pk=pk).first()
    context['product'] = product
    print(product)
    return render(request, 'core/product.html', context)

    # for category in category_qs:
    #     print('category', category.title)
    #     for product in category.product_set.all():
    #         print(product.title)
