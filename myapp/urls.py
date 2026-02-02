
from django.urls import path
from . import views

app_name = 'Myapp'

urlpatterns = [
    path('', views.post_client, name='Add')
]