from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
from django.template.response import TemplateResponse


def hello(request):
    # return HttpResponse('<center><h2>Roadtown Turkey Trot</h2></center>')
    return TemplateResponse(
        request, "trot2023bootstrap.html", {}
    )    


def hello2(request):
    return TemplateResponse(
        request, "trot2023.html", {}
    )    
