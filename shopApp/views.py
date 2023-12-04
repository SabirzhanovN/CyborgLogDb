from django.db import connection
from django.shortcuts import render
from .models import Product, LoggingMoves


def index(request):
    data = Product.objects.all()

    context = {'data': data}
    return render(request, 'shopApp/index.html', context)