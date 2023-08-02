# views.py
from django.shortcuts import redirect

def home(_):
    return redirect('/trot/', permanent=False)
