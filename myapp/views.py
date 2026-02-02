from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.db.models import Count
from . import models
from .forms import FormClient

def post_client(request: HttpRequest):
    if request.method == 'POST':
        formulario = FormClient(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Main:Home')

def total_clientes(request: HttpRequest):
    client = models.Order.objects.annotate(totalClient=Count('client'))