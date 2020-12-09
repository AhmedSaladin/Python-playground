from django.shortcuts import render

# Create your views here (The logic).

def home (req):
    return render(req,'blog/home.html')

def about(req):
        return render(req,'blog/about.html')

