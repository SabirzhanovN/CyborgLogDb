from django.db import connection
from django.shortcuts import render
from .models import Product, LoggingMoves
from config.clear_db import check_count_of_data, clear_db


def index(request):
    if check_count_of_data() > 100:
        clear_db()

    return render(request, 'shopApp/index.html')