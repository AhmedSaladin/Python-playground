from django.http import HttpResponse
from django.shortcuts import render

# Create your views here (The logic).

def home (req):
    return HttpResponse('<h1>Blog Home</h1>')

def about(req):
        return HttpResponse('<h1>Blog About</h1>')

