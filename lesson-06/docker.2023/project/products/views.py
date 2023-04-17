from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product

def product_index(request):
    products = Product.objects.all()
    return HttpResponse(f'Hello, products: [{"|".join(str(product) for product in products)}]')
