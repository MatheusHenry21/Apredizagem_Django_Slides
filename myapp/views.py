from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from . import models

def teste(request: HttpRequest):
    return HttpResponse(models.Order.objects.select_related('client'))