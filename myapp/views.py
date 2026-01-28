from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.db.models import Count
from . import models

def teste(request: HttpRequest):
    return HttpResponse(models.Order.objects.select_related('client').all())

def total_clientes(request: HttpRequest):
    client = models.Order.objects.annotate(totalClient=Count('client'))