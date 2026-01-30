from django.shortcuts import render
from django.http import HttpRequest
from django.db.models import Count
from . import models

def teste(request: HttpRequest):
    return render(request, 'index.html')

def total_clientes(request: HttpRequest):
    client = models.Order.objects.annotate(totalClient=Count('client'))