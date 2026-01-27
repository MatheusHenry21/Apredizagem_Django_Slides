from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def teste(request: HttpRequest):
    return HttpResponse('Vamos corinthians')