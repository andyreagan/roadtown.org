from django.urls import path

from .views import *

urlpatterns = [
    path('', hello, name='hello'),
    path('2', hello2, name='hello2'),
]

