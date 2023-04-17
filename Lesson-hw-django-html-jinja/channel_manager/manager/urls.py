from django.urls import path
from .views import *


urlpatterns = [
    path('', article, name='home'),
    path('middle/', article2, name='middle'),
    path('last/', article3, name='last'),
]
