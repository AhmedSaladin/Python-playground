from django.shortcuts import render
# Create your views here (The logic).


# Create dummy data to test
posts = [{
    'author': 'coryMs',
    'title': 'post 1',
    'content': 'First post content',
    'date_posted': 'august 27,2018'
},
    {
    'author': 'Jane Doe',
    'title': 'post 12',
    'content': 'Second post content',
    'date_posted': 'august 28,2018'
}]


def home(req):
    return render(req, 'blog/home.html')


def about(req):
    return render(req, 'blog/about.html')
